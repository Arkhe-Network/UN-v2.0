import React from 'react';
import { TrendingUp, ShieldAlert, PieChart, Landmark, ArrowUpRight, ArrowDownRight, Activity } from 'lucide-react';

const TokenomicsView = () => {
  const stats = [
    { label: "Total Staked (λΩ)", value: "752,401,922", change: "+1.2%", trend: "up" },
    { label: "Annual Emission", value: "1.00%", change: "Stable", trend: "neutral" },
    { label: "Handover Fees (24h)", value: "42,109 λΩ", change: "-5.4%", trend: "down" },
    { label: "Coherence Reserve", value: "12,500,000 λΩ", change: "+0.8%", trend: "up" },
  ];

  const parameters = [
    { name: "Active Node Reward", value: "100%", description: "Base rate for high-reputation nodes." },
    { name: "Standby Node Reward", value: "20%", description: "If T2* > 48μs (high-quality redundancy)." },
    { name: "Handover Fee", value: "0.5%", description: "Dynamic; based on degradation history." },
    { name: "Slashing (Critical)", value: "10%", description: "Penalty for non-reporting or failure." },
  ];

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-primary flex items-center gap-2">
          <Landmark className="w-6 h-6" />
          ARKHE-Ω TOKENOMICS (λΩ)
        </h2>
        <div className="flex gap-2">
          <span className="px-3 py-1 bg-primary/10 text-primary border border-primary/20 rounded-full text-xs font-mono">
            COHERENCE-STABLE: 98.4%
          </span>
        </div>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {stats.map((stat, i) => (
          <div key={i} className="bg-card border border-card-border p-4 rounded-lg">
            <p className="text-muted-foreground text-xs uppercase tracking-wider mb-1">{stat.label}</p>
            <div className="flex items-end justify-between">
              <span className="text-xl font-bold font-mono">{stat.value}</span>
              <span className={`text-xs flex items-center gap-1 ${
                stat.trend === 'up' ? 'text-green-500' : stat.trend === 'down' ? 'text-red-500' : 'text-muted-foreground'
              }`}>
                {stat.trend === 'up' && <ArrowUpRight className="w-3 h-3" />}
                {stat.trend === 'down' && <ArrowDownRight className="w-3 h-3" />}
                {stat.change}
              </span>
            </div>
          </div>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Economic Parameters */}
        <div className="lg:col-span-2 bg-card border border-card-border p-6 rounded-lg">
          <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Activity className="w-5 h-5 text-primary" />
            Economic Parameters (Berechman Model)
          </h3>
          <div className="space-y-4">
            {parameters.map((param, i) => (
              <div key={i} className="flex items-center justify-between p-3 bg-background/50 border border-card-border rounded">
                <div>
                  <p className="font-medium text-sm">{param.name}</p>
                  <p className="text-muted-foreground text-xs">{param.description}</p>
                </div>
                <div className="text-primary font-mono font-bold text-lg">
                  {param.value}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Stake Distribution / Risks */}
        <div className="space-y-6">
          <div className="bg-card border border-card-border p-6 rounded-lg">
            <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
              <PieChart className="w-5 h-5 text-primary" />
              Stake Distribution
            </h3>
            <div className="space-y-3">
              <div className="w-full bg-muted h-2 rounded-full overflow-hidden">
                <div className="bg-primary h-full w-[70%]" />
              </div>
              <div className="flex justify-between text-xs">
                <span className="flex items-center gap-1">
                  <span className="w-2 h-2 rounded-full bg-primary" /> Active Nodes (70%)
                </span>
                <span className="flex items-center gap-1">
                  <span className="w-2 h-2 rounded-full bg-muted" /> Standby/Treasury (30%)
                </span>
              </div>
            </div>
          </div>

          <div className="bg-card border border-card-border p-6 rounded-lg border-l-4 border-l-red-500/50">
            <h3 className="text-lg font-semibold mb-2 flex items-center gap-2 text-red-400">
              <ShieldAlert className="w-5 h-5" />
              Coherence Risks
            </h3>
            <ul className="text-xs space-y-2 text-muted-foreground">
              <li className="flex justify-between">
                <span>Natural T2* Decay (Annual):</span>
                <span className="text-foreground font-mono">0.5%</span>
              </li>
              <li className="flex justify-between">
                <span>Free-Rider Threshold:</span>
                <span className="text-foreground font-mono">&lt; 500k λΩ</span>
              </li>
              <li className="flex justify-between">
                <span>Infrastructure Rust Index:</span>
                <span className="text-yellow-500 font-mono">LOW (2.4%)</span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      {/* Simulation Banner */}
      <div className="bg-primary/5 border border-primary/20 p-4 rounded-lg flex items-center justify-between">
        <div className="flex items-center gap-3">
          <TrendingUp className="w-6 h-6 text-primary" />
          <div>
            <p className="font-semibold text-sm">10-Year Coherence Horizon Simulation</p>
            <p className="text-xs text-muted-foreground">Scenario A (Steady State) active. R(t) projected to remain > 0.95 until 2034.</p>
          </div>
        </div>
        <button className="px-4 py-2 bg-primary text-background rounded font-bold text-xs hover:bg-primary/90 transition-colors">
          RUN NEW SIMULATION
        </button>
      </div>
    </div>
  );
};

export default TokenomicsView;
