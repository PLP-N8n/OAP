import React from 'react';
import { AlertTriangle, Shield, Eye } from 'lucide-react';

const risks = [
  {
    title: 'AI Hallucination',
    mitigation:
      'Citation anchoring forces every finding to map to a rule ID. If there is no citation, the system refuses to proceed.',
    icon: AlertTriangle,
  },
  {
    title: 'Perceived Bias',
    mitigation:
      'Radical visibility exposes the rule and the reasoning, keeping the debate on policy, not on the system.',
    icon: Eye,
  },
  {
    title: 'Regulatory Exposure',
    mitigation:
      'Norm-agnostic positioning keeps OAP procedural rather than moral, reducing liability.',
    icon: Shield,
  },
];

export const Risks: React.FC = () => {
  return (
    <section id="risks" className="py-24 bg-ink-950">
      <div className="container mx-auto px-6">
        <div className="text-center mb-12">
          <span className="text-teal-300 font-mono text-xs tracking-[0.3em] uppercase">Risks</span>
          <h2 className="text-3xl md:text-4xl font-bold text-white mt-3">Risks & Mitigations</h2>
          <p className="text-slate-400 mt-4 max-w-2xl mx-auto">
            The protocol is engineered for transparency-first safety and auditability.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          {risks.map((risk) => (
            <div key={risk.title} className="glass-panel p-6 rounded-2xl border border-slate-800/80">
              <div className="w-12 h-12 rounded-xl bg-teal-500/10 flex items-center justify-center mb-4">
                <risk.icon className="w-6 h-6 text-teal-300" />
              </div>
              <h3 className="text-xl font-semibold text-white mb-3">{risk.title}</h3>
              <p className="text-sm text-slate-400 leading-relaxed">{risk.mitigation}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
