import React from 'react';
import { UploadCloud, Network, FileCheck } from 'lucide-react';

export const HowItWorks: React.FC = () => {
  const steps = [
    {
      icon: <UploadCloud className="w-8 h-8 text-teal-300" />,
      title: "1. Ingest",
      desc: "Upload your raw Terms of Service. The Rulebook Normalizer converts them into a machine-readable constitution."
    },
    {
      icon: <Network className="w-8 h-8 text-sky-300" />,
      title: "2. Connect",
      desc: "Send disputed content via the API. The engine scans your normalized constitution for matches."
    },
    {
      icon: <FileCheck className="w-8 h-8 text-amber-300" />,
      title: "3. Resolve",
      desc: "Receive structured JSON containing the verdict, reasoning, and the citation anchor."
    }
  ];

  return (
    <section className="py-24 bg-ink-950">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <span className="text-xs uppercase tracking-[0.3em] text-slate-400">Protocol Flow</span>
          <h2 className="font-display text-3xl md:text-4xl font-semibold text-white mt-4">
            From chaos to order in three moves
          </h2>
          <p className="text-slate-400 mt-4 max-w-2xl mx-auto">
            Clear stages, auditable outputs, and zero guessing.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-12 relative">
          <div className="hidden md:block absolute top-12 left-[16%] right-[16%] h-0.5 bg-gradient-to-r from-transparent via-teal-500/30 to-transparent border-t border-dashed border-slate-700 -z-10" />

          {steps.map((step, idx) => (
            <div key={idx} className="relative flex flex-col items-center text-center group">
              <div className="w-24 h-24 glass-panel rounded-full flex items-center justify-center mb-6 shadow-[0_0_30px_rgba(45,212,191,0.12)] group-hover:scale-105 transition-transform duration-300 bg-ink-900">
                {step.icon}
              </div>
              <h3 className="text-xl font-semibold text-white mb-3">{step.title}</h3>
              <p className="text-slate-400 px-4">{step.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
