import React from 'react';
import { UploadCloud, Network, FileCheck } from 'lucide-react';

export const HowItWorks: React.FC = () => {
  const steps = [
    {
      icon: <UploadCloud className="w-8 h-8 text-blue-400" />,
      title: "1. Ingest",
      desc: "Upload your raw Terms of Service or Community Guidelines. Our Rulebook Normalizer converts them into a machine-readable Constitution."
    },
    {
      icon: <Network className="w-8 h-8 text-purple-400" />,
      title: "2. Connect",
      desc: "Send disputed content via our API. The engine scans your normalized constitution for semantic matches."
    },
    {
      icon: <FileCheck className="w-8 h-8 text-green-400" />,
      title: "3. Resolve",
      desc: "Receive a structured JSON output containing the verdict, the reasoning, and the Citation Anchor."
    }
  ];

  return (
    <section className="py-24 bg-slate-950">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-3xl font-bold text-white">From Chaos to Order in 3 Steps</h2>
        </div>
        
        <div className="grid md:grid-cols-3 gap-12 relative">
            {/* Connecting line for desktop */}
            <div className="hidden md:block absolute top-12 left-[16%] right-[16%] h-0.5 bg-gradient-to-r from-blue-500/0 via-blue-500/30 to-blue-500/0 border-t border-dashed border-slate-700 -z-1" />

          {steps.map((step, idx) => (
            <div key={idx} className="relative flex flex-col items-center text-center group">
              <div className="w-24 h-24 glass-panel rounded-full flex items-center justify-center mb-6 shadow-[0_0_30px_rgba(59,130,246,0.1)] group-hover:scale-110 transition-transform duration-300 bg-slate-900">
                {step.icon}
              </div>
              <h3 className="text-xl font-bold text-white mb-3">{step.title}</h3>
              <p className="text-slate-400 px-4">{step.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};