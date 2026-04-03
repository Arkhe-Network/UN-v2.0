import React from 'react';
import { Zap, GitBranch, Key, Search, FileText, Database } from 'lucide-react';

const NIPCard = ({ nip, role, description, icon: Icon, colorClass }) => (
  <div className="flex flex-col p-4 rounded-xl border bg-card hover:border-primary/50 transition-colors shadow-sm">
    <div className="flex items-center justify-between mb-3">
      <div className={`p-2 rounded-lg bg-opacity-10 ${colorClass.replace('text-', 'bg-')}`}>
        <Icon className={`w-5 h-5 ${colorClass}`} />
      </div>
      <span className="text-xs font-mono font-bold bg-muted px-2 py-1 rounded">NIP-{nip}</span>
    </div>
    <h3 className="font-semibold text-sm mb-1">{role}</h3>
    <p className="text-xs text-muted-foreground leading-relaxed">{description}</p>
  </div>
);

const NIPSubnets = () => {
  const subnets = [
    { nip: '01', role: 'Identity Subnet', description: 'Base protocol and identity relaying.', icon: Key, colorClass: 'text-amber-500' },
    { nip: '34', role: 'Git Subnet', description: 'Sovereign version control for projects.', icon: GitBranch, colorClass: 'text-purple-500' },
    { nip: '46', role: 'Remote Signer', description: 'Delegated jurisdictional signing.', icon: Zap, colorClass: 'text-yellow-500' },
    { nip: '89', role: 'Discovery Subnet', description: 'Dynamic indexing of governance nodes.', icon: Search, colorClass: 'text-blue-500' },
    { nip: '94', role: 'Storage Subnet', description: 'Decentralized jurisdictional data.', icon: Database, colorClass: 'text-emerald-500' },
    { nip: '04', role: 'Confidentiality', description: 'Encrypted governance communication.', icon: FileText, colorClass: 'text-rose-500' },
  ];

  return (
    <div className="mb-8">
      <h2 className="text-lg font-bold mb-4 flex items-center gap-2">
        Governance Subnets <span className="text-xs font-normal text-muted-foreground">(Mesh-LLM)</span>
      </h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {subnets.map((s) => <NIPCard key={s.nip} {...s} />)}
      </div>
    </div>
  );
};

export default NIPSubnets;
