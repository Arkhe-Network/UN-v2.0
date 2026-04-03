import React from 'react';
import SystemStatus from './components/SystemStatus';
import NIPSubnets from './components/NIPSubnets';
import AgentSkills from './components/AgentSkills';
import RecentProjects from './components/RecentProjects';
import RoadmapTracker from './components/RoadmapTracker';
import DeploymentHub from './components/DeploymentHub';
import HandoverMonitor from './components/HandoverMonitor';
import TokenomicsView from './components/TokenomicsView';

const App = () => {
  return (
    <div className="min-h-screen bg-background text-foreground font-sans p-6 md:p-12">
      <header className="mb-12">
        <div className="flex items-center gap-3 mb-2 text-primary">
          <div className="w-8 h-8 rounded bg-primary/20 flex items-center justify-center font-bold">🜏</div>
          <h1 className="text-2xl font-black tracking-tighter uppercase">UN-v2.0 / ONU 2.0</h1>
        </div>
        <p className="text-muted-foreground text-sm max-w-2xl">
          Plataforma de governança multi-nível com controle jurisdicional por GPS e Mesh-LLM.
          Sincronizando a soberania digital com a coerência do $\tau$-field.
        </p>
      </header>

      <SystemStatus />

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <TokenomicsView />
          <DeploymentHub />
          <HandoverMonitor />
          <NIPSubnets />
          <RecentProjects />
        </div>
        <aside className="space-y-8">
          <AgentSkills />
          <RoadmapTracker />
          <div className="p-6 rounded-xl border bg-primary/5 border-primary/20">
            <h3 className="text-sm font-bold mb-2 uppercase tracking-wide">AO Message Feed</h3>
            <div className="space-y-3 font-mono text-[10px]">
              <div className="p-2 rounded bg-background/50 border border-primary/10">
                <span className="text-primary font-bold">INIT</span> → AO_GPS_AGI_PID [delivered]
              </div>
              <div className="p-2 rounded bg-background/50 border border-primary/10">
                <span className="text-primary font-bold">VALIDATE</span> → JURISDICTION_7X [delivered]
              </div>
              <div className="p-2 rounded bg-background/50 border border-primary/10">
                <span className="text-status-pending">PROCESS</span> → COMPLIANCE_LEDGER [sent]
              </div>
            </div>
          </div>
        </aside>
      </div>

      <footer className="mt-16 pt-8 border-t border-muted text-[10px] text-muted-foreground flex justify-between uppercase tracking-widest">
        <span>Arkhe-Network / UN-v2.0</span>
        <span>Coherence Phase: Coherent-Blue</span>
        <span>Network: Bitcoin-Satoshi</span>
      </footer>
    </div>
  );
};

export default App;
