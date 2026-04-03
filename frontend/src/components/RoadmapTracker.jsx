import React from 'react';
import { Map, CheckCircle2, Circle } from 'lucide-react';

const RoadmapItem = ({ track, progress, status }) => (
  <div className="flex flex-col gap-2 p-3 rounded-lg border bg-card/30">
    <div className="flex items-center justify-between">
      <span className="text-xs font-bold uppercase tracking-tighter">{track}</span>
      <span className="text-[10px] text-muted-foreground">{progress}%</span>
    </div>
    <div className="w-full h-1.5 bg-muted rounded-full overflow-hidden">
      <div
        className="h-full bg-primary transition-all duration-500"
        style={{ width: `${progress}%` }}
      />
    </div>
    <div className="flex items-center gap-1.5 text-[10px] text-muted-foreground">
      {status === 'Complete' ? <CheckCircle2 className="w-3 h-3 text-primary" /> : <Circle className="w-3 h-3" />}
      {status}
    </div>
  </div>
);

const RoadmapTracker = () => {
  const tracks = [
    { track: "AI Engineer (Mesh-LLM)", progress: 85, status: "Optimizing" },
    { track: "Backend (AO Gateway)", progress: 92, status: "Stabilized" },
    { track: "AI Agents (Goose/MCP)", progress: 64, status: "Arborizing" },
    { track: "DevOps (Mesh Ops)", progress: 45, status: "Provisioning" },
  ];

  return (
    <div className="p-6 rounded-xl border bg-card shadow-sm">
      <h2 className="text-lg font-bold mb-6 flex items-center gap-2">
        <Map className="w-5 h-5 text-sky-500" />
        Agentic Roadmaps
      </h2>
      <div className="space-y-4">
        {tracks.map((t) => <RoadmapItem key={t.track} {...t} />)}
      </div>
      <button className="w-full mt-6 py-2 rounded-lg bg-muted hover:bg-muted/80 text-xs font-semibold transition-colors">
        View All Paths (roadmap.sh)
      </button>
    </div>
  );
};

export default RoadmapTracker;
