package skills

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

// Skill represents a specialized subnet/subagent discovered in the system.
type Skill struct {
	Name        string
	Version     string
	Description string
	Path        string
	Executable  string
}

// Registry manages the discovery and routing of subagents (skills).
type Registry struct {
	skills map[string]*Skill
}

// NewRegistry creates and initializes a new Skill Registry.
func NewRegistry(skillsDir string) (*Registry, error) {
	reg := &Registry{
		skills: make(map[string]*Skill),
	}

	err := reg.Discover(skillsDir)
	if err != nil {
		return nil, err
	}

	return reg, nil
}

// Discover crawls the skills directory for subagents (subnets).
func (r *Registry) Discover(dir string) error {
	entries, err := os.ReadDir(dir)
	if err != nil {
		if os.IsNotExist(err) {
			return nil
		}
		return err
	}

	for _, entry := range entries {
		if entry.IsDir() {
			skillPath := filepath.Join(dir, entry.Name())
			skill, err := r.parseSkill(skillPath)
			if err != nil {
				// Log error but continue with other skills
				fmt.Printf("Warning: failed to parse skill in %s: %v\n", skillPath, err)
				continue
			}
			r.skills[skill.Name] = skill
		}
	}
	return nil
}

func (r *Registry) parseSkill(path string) (*Skill, error) {
	// Simple parser for metadata (SKILL.md)
	data, err := os.ReadFile(filepath.Join(path, "SKILL.md"))
	if err != nil {
		return nil, err
	}

	skill := &Skill{Path: path}
	lines := strings.Split(string(data), "\n")
	for _, line := range lines {
		parts := strings.SplitN(line, ":", 2)
		if len(parts) < 2 {
			continue
		}
		key := strings.TrimSpace(parts[0])
		val := strings.TrimSpace(parts[1])
		val = strings.Trim(val, "\"")

		switch key {
		case "name":
			skill.Name = val
		case "version":
			skill.Version = val
		case "description":
			skill.Description = val
		}
	}

	// Determine executable based on convention
	pyFile := filepath.Join(path, skill.Name+".py")
	if _, err := os.Stat(pyFile); err == nil {
		skill.Executable = "python3 " + pyFile
	}

	if skill.Name == "" {
		return nil, fmt.Errorf("skill name missing in metadata")
	}

	return skill, nil
}

// GetSkill returns a skill by its unique name (subnet identifier).
func (r *Registry) GetSkill(name string) (*Skill, bool) {
	s, ok := r.skills[name]
	return s, ok
}

// ListSkills returns all discovered subagents.
func (r *Registry) ListSkills() []*Skill {
	var list []*Skill
	for _, s := range r.skills {
		list = append(list, s)
	}
	return list
}
