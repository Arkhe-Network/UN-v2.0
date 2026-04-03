import React from 'react';
import { Activity, MapPin, ShieldCheck, Cpu } from 'lucide-react';

const StatusItem = ({ icon: Icon, label, status, colorClass }) => (
  <div className="flex items-center gap-2 p-3 rounded-lg border bg-card/50">
    <Icon className={`w-5 h-5 ${colorClass}`} />
    <div className="flex flex-col">
      <span className="text-xs text-muted-foreground uppercase tracking-wider">{label}</span>
      <span className="text-sm font-semibold">{status}</span>
    </div>
  </div>
);

const SystemStatus = () => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
      <StatusItem
        icon={Activity}
        label="AO Gateway"
        status="Operacional"
        colorClass="text-emerald-500"
      />
      <StatusItem
        icon={MapPin}
        label="GPS Validator"
        status="Sincronizado"
        colorClass="text-emerald-500"
      />
      <StatusItem
        icon={ShieldCheck}
        label="Compliance Ledger"
        status="Ativo"
        colorClass="text-emerald-500"
      />
      <StatusItem
        icon={Cpu}
        label="Mesh-LLM (Bittensor)"
        status="Coerente"
        colorClass="text-sky-500"
      />
    </div>
  );
};

export default SystemStatus;
