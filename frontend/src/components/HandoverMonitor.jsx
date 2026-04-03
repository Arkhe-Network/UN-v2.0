import React from 'react';
import { Share2, ArrowRightLeft, ShieldAlert, CheckCircle } from 'lucide-react';

const HandoverMonitor = () => {
  return (
    <div className="p-6 rounded-xl border bg-card shadow-sm border-amber-500/30">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-lg font-bold flex items-center gap-2 text-amber-500">
          <Share2 className="w-5 h-5" />
          Quantum Handover (Node_R → Node_S)
        </h2>
        <span className="text-[10px] font-bold bg-amber-500/10 text-amber-500 px-2 py-1 rounded uppercase tracking-widest animate-pulse">
          In Progress
        </span>
      </div>

      <div className="space-y-6">
        {/* Memory Teleportation */}
        <div className="space-y-2">
          <div className="flex justify-between items-end">
            <span className="text-xs font-bold uppercase tracking-tight">Quantum Memory Teleportation</span>
            <span className="text-[10px] text-muted-foreground">72% complete</span>
          </div>
          <div className="w-full h-2 bg-muted rounded-full overflow-hidden">
            <div className="h-full bg-amber-500 w-[72%] transition-all duration-1000" />
          </div>
          <div className="flex justify-between text-[8px] font-mono text-muted-foreground">
            <span>Bell Measurement: SUCCESS</span>
            <span>Correction: Pauli-XZ Applied</span>
          </div>
        </div>

        {/* Identity & Stake */}
        <div className="p-3 rounded-lg bg-background/50 border border-muted space-y-3">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <ArrowRightLeft className="w-4 h-4 text-sky-500" />
              <span className="text-xs font-semibold">Identity Reassignment</span>
            </div>
            <CheckCircle className="w-3 h-3 text-emerald-500" />
          </div>
          <div className="grid grid-cols-2 gap-2 text-[10px]">
            <div className="flex flex-col">
              <span className="text-muted-foreground">MuSig2 Quorum</span>
              <span className="font-bold text-emerald-500">6/9 Approved</span>
            </div>
            <div className="flex flex-col items-end">
              <span className="text-muted-foreground">Stake Transfer</span>
              <span className="font-bold text-emerald-500">Confirmed (λΩ)</span>
            </div>
          </div>
        </div>

        {/* Critical Alerts */}
        <div className="flex items-start gap-3 p-3 rounded-lg bg-rose-500/5 border border-rose-500/20">
          <ShieldAlert className="w-4 h-4 text-rose-500 shrink-0 mt-0.5" />
          <div className="flex flex-col">
            <span className="text-xs font-bold text-rose-500">Coexistence Period (24h)</span>
            <p className="text-[10px] text-muted-foreground leading-tight">
              Dual routing active. Node_R remains primary until T-minus 14:22:10.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HandoverMonitor;
