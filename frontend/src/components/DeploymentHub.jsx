import React from 'react';
import { Package, Coffee, Terminal, Gem, Box, Boxes } from 'lucide-react';

const RegistryItem = ({ subagent, registry, ecosystem, icon: Icon, colorClass, status }) => (
  <div className="p-4 rounded-xl border bg-card/50 hover:bg-card transition-all group">
    <div className="flex items-start justify-between mb-3">
      <div className={`p-2 rounded-lg bg-opacity-10 ${colorClass.replace('text-', 'bg-')}`}>
        <Icon className={`w-5 h-5 ${colorClass}`} />
      </div>
      <div className="flex flex-col items-end">
        <span className="text-[10px] font-mono text-muted-foreground uppercase">{registry}</span>
        <div className="flex items-center gap-1.5 mt-1">
          <div className={`w-1.5 h-1.5 rounded-full ${status === 'Ready' ? 'bg-primary' : 'bg-status-pending'} animate-pulse`} />
          <span className="text-[10px] font-bold uppercase">{status}</span>
        </div>
      </div>
    </div>
    <h3 className="font-bold text-sm mb-1">{subagent}</h3>
    <p className="text-[10px] text-muted-foreground leading-tight uppercase tracking-widest">{ecosystem}</p>
  </div>
);

const DeploymentHub = () => {
  const registries = [
    { subagent: "Arbor-NPM", registry: "npm", ecosystem: "JavaScript / Node.js", icon: Package, colorClass: "text-rose-500", status: "Ready" },
    { subagent: "Arbor-Maven", registry: "Maven Central", ecosystem: "Java / JRE", icon: Coffee, colorClass: "text-orange-500", status: "Ready" },
    { subagent: "Arbor-NuGet", registry: "NuGet", ecosystem: ".NET / MSFT", icon: Boxes, colorClass: "text-blue-500", status: "Ready" },
    { subagent: "Arbor-Gems", registry: "RubyGems", ecosystem: "Ruby", icon: Gem, colorClass: "text-rose-600", status: "Ready" },
    { subagent: "Arbor-Container", registry: "Docker Hub / OCI", ecosystem: "Container Images", icon: Box, colorClass: "text-sky-500", status: "Ready" },
  ];

  return (
    <div className="mb-8">
      <h2 className="text-lg font-bold mb-4 flex items-center gap-2">
        <Terminal className="w-5 h-5 text-primary" />
        Deployment Hub (Autonomous Launch)
      </h2>
      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
        {registries.map((r) => <RegistryItem key={r.subagent} {...r} />)}
      </div>
    </div>
  );
};

export default DeploymentHub;
