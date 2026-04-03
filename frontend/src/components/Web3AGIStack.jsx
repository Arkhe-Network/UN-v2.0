import React from 'react';
import {
  Database,
  Fingerprint,
  Coins,
  Brain,
  Cpu,
  HardDrive,
  Landmark,
  ShieldCheck,
  ChevronRight
} from 'lucide-react';

const layers = [
  {
    id: 7,
    name: "Marketplace & Governance",
    icon: Landmark,
    description: "Coordination, dynamic reputation, and DAO control.",
    tools: ["Aragon", "Snapshot", "Quasar"],
    color: "text-purple-400",
    bg: "bg-purple-400/10"
  },
  {
    id: 6,
    name: "Storage & Provenance",
    icon: HardDrive,
    description: "Permanent model storage and verifiable audit trails.",
    tools: ["Arweave", "IPFS", "Filecoin"],
    color: "text-blue-400",
    bg: "bg-blue-400/10"
  },
  {
    id: 5,
    name: "Execution & Compute",
    icon: Cpu,
    description: "Verifiable inference (TEEs) and DePIN scale.",
    tools: ["Intel SGX", "Akash", "NVIDIA TEE"],
    color: "text-orange-400",
    bg: "bg-orange-400/10"
  },
  {
    id: 4,
    name: "Intelligence & Agent",
    icon: Brain,
    description: "Hybrid LLM logic (Planner/Executor) and skills.",
    tools: ["Jupiter CLI", "WASM Plugins", "Vector DB"],
    color: "text-pink-400",
    bg: "bg-pink-400/10"
  },
  {
    id: 3,
    name: "Payments & Micropayments",
    icon: Coins,
    description: "Machine economics via MPP/x402 HTTP 402 flow.",
    tools: ["mpp-sdk", "Solana", "x402"],
    color: "text-yellow-400",
    bg: "bg-yellow-400/10"
  },
  {
    id: 2,
    name: "Identity & Wallet",
    icon: Fingerprint,
    description: "Local-first OWS key custody and policy gating.",
    tools: ["OWS SDK", "OWS CLI", "mTLS"],
    color: "text-primary",
    bg: "bg-primary/10"
  },
  {
    id: 1,
    name: "Data & Indexing",
    icon: Database,
    description: "Real-time and historical on-chain state access.",
    tools: ["The Graph", "Substreams", "Geyser"],
    color: "text-cyan-400",
    bg: "bg-cyan-400/10"
  }
];

const Web3AGIStack = () => {
  return (
    <div className="bg-card border border-card-border rounded-xl p-6 mb-8">
      <div className="flex items-center justify-between mb-6">
        <div>
          <h2 className="text-xl font-bold text-foreground flex items-center gap-2">
            <ShieldCheck className="w-5 h-5 text-primary" />
            WEB3 AGI ARCHITECTURE STACK
          </h2>
          <p className="text-muted-foreground text-xs mt-1 uppercase tracking-widest">
            Modular multi-layer framework for autonomous agents
          </p>
        </div>
        <div className="px-3 py-1 bg-primary/10 border border-primary/20 rounded-full text-[10px] text-primary font-mono font-bold">
          v2.0-SOVEREIGN
        </div>
      </div>

      <div className="space-y-3">
        {layers.map((layer) => (
          <div
            key={layer.id}
            className="group flex items-start gap-4 p-4 rounded-lg border border-card-border bg-background/50 hover:border-primary/30 transition-all cursor-default"
          >
            <div className={`p-2 rounded-md ${layer.bg} ${layer.color}`}>
              <layer.icon className="w-5 h-5" />
            </div>

            <div className="flex-1 min-w-0">
              <div className="flex items-center justify-between">
                <h3 className="text-sm font-bold text-foreground">
                  Layer {layer.id}: {layer.name}
                </h3>
                <div className="flex gap-1">
                  {layer.tools.map((tool, idx) => (
                    <span key={idx} className="text-[9px] px-1.5 py-0.5 rounded bg-muted text-muted-foreground font-mono">
                      {tool}
                    </span>
                  ))}
                </div>
              </div>
              <p className="text-xs text-muted-foreground mt-1 line-clamp-1">
                {layer.description}
              </p>
            </div>

            <div className="text-muted opacity-0 group-hover:opacity-100 transition-opacity self-center">
              <ChevronRight className="w-4 h-4" />
            </div>
          </div>
        ))}
      </div>

      <div className="mt-6 p-4 rounded-lg border border-dashed border-primary/20 bg-primary/5">
        <h4 className="text-[10px] font-bold text-primary uppercase tracking-tighter mb-2 flex items-center gap-2">
          <ChevronRight className="w-3 h-3" />
          Core Protocol Integration (OWS + MPP)
        </h4>
        <p className="text-[11px] text-muted-foreground leading-relaxed">
          The stack integrates **Open Wallet Standard** for secure key isolation and
          **Machine Payments Protocol** for autonomous economic transactions.
          Agents operate via HTTP 402 handshakes, checking OWS policies before every on-chain interaction.
        </p>
      </div>
    </div>
  );
};

export default Web3AGIStack;
