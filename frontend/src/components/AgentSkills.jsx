import React from 'react';
import { TreePine, Plus, Star } from 'lucide-react';

const SkillNode = ({ label, level }) => (
  <div className="flex items-center justify-between py-2 border-b last:border-0 border-muted">
    <span className="text-sm font-medium">{label}</span>
    <div className="flex gap-0.5">
      {[1, 2, 3, 4, 5].map((i) => (
        <Star
          key={i}
          className={`w-3 h-3 ${i <= level ? 'text-primary fill-primary' : 'text-muted'}`}
        />
      ))}
    </div>
  </div>
);

const AgentSkills = () => {
  return (
    <div className="p-6 rounded-xl border bg-card shadow-sm">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-lg font-bold flex items-center gap-2">
          <TreePine className="w-5 h-5 text-emerald-600" />
          Skill Arborization
        </h2>
        <button className="p-1.5 rounded-full bg-primary/10 text-primary hover:bg-primary/20 transition-colors">
          <Plus className="w-4 h-4" />
        </button>
      </div>

      <div className="space-y-1">
        <h3 className="text-xs font-bold text-muted-foreground uppercase mb-2 tracking-tighter">Active MCP Tools</h3>
        <SkillNode label="sign_governance_event" level={5} />
        <SkillNode label="verify_gps_coordinates" level={4} />
        <SkillNode label="check_smc_v2_status" level={4} />
        <SkillNode label="allocate_agent_resources" level={3} />
        <SkillNode label="discover_mesh_nodes" level={2} />
      </div>
    </div>
  );
};

export default AgentSkills;
