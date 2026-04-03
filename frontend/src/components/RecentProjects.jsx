import React from 'react';
import { ExternalLink } from 'lucide-react';

const ProjectCard = ({ id, title, description, status, code }) => (
  <div className="p-4 rounded-lg border bg-card/50 hover:bg-card transition-colors group">
    <div className="flex items-start justify-between mb-2">
      <h3 className="font-semibold text-sm group-hover:text-primary transition-colors">{title}</h3>
      <span className={`text-[10px] font-bold px-2 py-0.5 rounded uppercase ${
        status === 'Approved' ? 'bg-emerald-500/10 text-emerald-500' : 'bg-rose-500/10 text-rose-500'
      }`}>
        {status}
      </span>
    </div>
    <p className="text-xs text-muted-foreground mb-3 line-clamp-2 leading-relaxed">{description}</p>
    <div className="flex items-center justify-between text-[10px] font-mono text-muted-foreground">
      <span>{code}</span>
      <ExternalLink className="w-3 h-3 opacity-0 group-hover:opacity-100 transition-opacity" />
    </div>
  </div>
);

const RecentProjects = () => {
  const projects = [
    {
      id: 1,
      title: "Rede Nacional de Compliance AO",
      description: "Infraestrutura distribuída para validação de compliance em projetos culturais.",
      status: "Approved",
      code: "SMC-2025/PROJ-7X8Y9Z"
    },
    {
      id: 2,
      title: "Sistema AGI de Monitoramento Urbano",
      description: "Plataforma de inteligência artificial para monitoramento em tempo real de infraestrutura urbana.",
      status: "Approved",
      code: "SMC-2025/PROJ-4T5N6P"
    },
    {
      id: 3,
      title: "Hub Cultural Carioca Digital",
      description: "Plataforma digital de catalogação e distribuição de conteúdo cultural carioca.",
      status: "Rejected",
      code: "SMC-2025/PROJ-2B3C4D"
    },
  ];

  return (
    <div className="flex-1">
      <h2 className="text-lg font-bold mb-4">Projetos Recentes</h2>
      <div className="grid grid-cols-1 gap-3">
        {projects.map((p) => <ProjectCard key={p.id} {...p} />)}
      </div>
    </div>
  );
};

export default RecentProjects;
