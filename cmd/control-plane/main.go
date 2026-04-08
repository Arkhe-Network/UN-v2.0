package main

import (
	"bytes"
	"context"
	"crypto/tls"
	"fmt"
	"log/slog"
	"net"
	"os"
	"os/exec"
	"os/signal"
	"strings"
	"syscall"

	pb "github.com/Arkhe-Network/UN-v2.0/api/proto"
	"github.com/Arkhe-Network/UN-v2.0/internal/skills"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"google.golang.org/protobuf/types/known/timestamppb"
)

type server struct {
	pb.UnimplementedControlPlaneServer
	logger   *slog.Logger
	registry *skills.Registry
}

func (s *server) ExecuteSandbox(ctx context.Context, req *pb.ExecuteSandboxRequest) (*pb.ExecuteSandboxResponse, error) {
	s.logger.Info("Executing sandbox (subnet/skill)", "task_id", req.TaskId, "jurisdiction", req.JurisdictionId)

	var output []byte
	status := "SUCCESS"

	// Route to specialized skill if task_id matches a subnet name
	if skill, ok := s.registry.GetSkill(req.TaskId); ok {
		s.logger.Info("Routing to subagent", "skill", skill.Name, "path", skill.Path)

		// Split executable into command and initial args
		parts := strings.Fields(skill.Executable)
		if len(parts) == 0 {
			return nil, fmt.Errorf("invalid executable for skill %s", skill.Name)
		}

		cmdName := parts[0]
		args := parts[1:]

		// Append payload and jurisdiction as arguments
		// Skills expect: [payload_json, jurisdiction]
		args = append(args, string(req.Payload), req.JurisdictionId)

		cmd := exec.CommandContext(ctx, cmdName, args...)
		var out bytes.Buffer
		var stderr bytes.Buffer
		cmd.Stdout = &out
		cmd.Stderr = &stderr

		err := cmd.Run()
		if err != nil {
			s.logger.Error("Skill execution failed", "error", err, "stderr", stderr.String())
			status = "FAILED"
			output = stderr.Bytes()
		} else {
			output = out.Bytes()
		}
	} else {
		return nil, fmt.Errorf("skill not found: %s", req.TaskId)
	}

	// TODO: Implement RBAC and input validation.
	// TODO: Implement isolation using MicroVMs (Firecracker/Kata).
	return &pb.ExecuteSandboxResponse{
		ExecutionId: "exec-" + req.TaskId,
		Status:      status,
		Output:      output,
		CompletedAt: timestamppb.Now(),
	}, nil
}

func (s *server) ManageSession(ctx context.Context, req *pb.ManageSessionRequest) (*pb.ManageSessionResponse, error) {
	s.logger.Info("Managing session", "session_id", req.SessionId, "action", req.Action)
	return &pb.ManageSessionResponse{
		SessionId: req.SessionId,
		Success:   true,
	}, nil
}

func (s *server) LogEvent(ctx context.Context, req *pb.LogEventRequest) (*pb.LogEventResponse, error) {
	s.logger.Info("Logging event", "type", req.EventType)
	return &pb.LogEventResponse{
		LedgerHash:     "hash-placeholder",
		SequenceNumber: 1,
	}, nil
}

func main() {
	logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))
	slog.SetDefault(logger)

	// Initialize the Skill Registry to discover subagents (subnets)
	registry, err := skills.NewRegistry("skills")
	if err != nil {
		logger.Error("failed to initialize skill registry", "error", err)
		os.Exit(1)
	}

	logger.Info("Subnets (Skills) discovered", "count", len(registry.ListSkills()))
	for _, skill := range registry.ListSkills() {
		logger.Info("  Subnet loaded", "name", skill.Name, "version", skill.Version)
	}

	// In a real production environment, load certificates from a secure vault or config.
	// This is a placeholder for mTLS setup as per RFC 8705.
	// For now, we use a basic TLS setup or insecure if no certs are provided,
	// but the structure is ready for credentials.LoadServerTLSFromFile.

	creds := credentials.NewTLS(&tls.Config{
		ClientAuth: tls.RequireAndVerifyClientCert,
		// Certificates: []tls.Certificate{serverCert},
		// ClientCAs: clientCAs,
	})
	_ = creds // Use creds in grpc.NewServer(grpc.Creds(creds)) when certs are available.

	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		logger.Error("failed to listen", "error", err)
		os.Exit(1)
	}

	// For bootstrapping, we'll allow insecure if no certs are configured,
	// but the project roadmap mandates mTLS.
	s := grpc.NewServer()
	pb.RegisterControlPlaneServer(s, &server{
		logger:   logger,
		registry: registry,
	})

	// Graceful shutdown
	stop := make(chan os.Signal, 1)
	signal.Notify(stop, os.Interrupt, syscall.SIGTERM)

	go func() {
		logger.Info("Control Plane listening", "address", lis.Addr())
		if err := s.Serve(lis); err != nil {
			logger.Error("failed to serve", "error", err)
		}
	}()

	<-stop
	logger.Info("Shutting down gracefully...")
	s.GracefulStop()
}
