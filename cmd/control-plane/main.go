package main

import (
	"context"
	"crypto/tls"
	"log/slog"
	"net"
	"os"
	"os/signal"
	"syscall"

	pb "github.com/Arkhe-Network/UN-v2.0/api/proto"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"google.golang.org/protobuf/types/known/timestamppb"
)

type server struct {
	pb.UnimplementedControlPlaneServer
	logger *slog.Logger
}

func (s *server) ExecuteSandbox(ctx context.Context, req *pb.ExecuteSandboxRequest) (*pb.ExecuteSandboxResponse, error) {
	s.logger.Info("Executing sandbox", "task_id", req.TaskId, "jurisdiction", req.JurisdictionId)
	// TODO: Implement RBAC and input validation.
	// TODO: Implement isolation using MicroVMs (Firecracker/Kata).
	return &pb.ExecuteSandboxResponse{
		ExecutionId: "exec-placeholder",
		Status:      "SUCCESS",
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
	pb.RegisterControlPlaneServer(s, &server{logger: logger})

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
