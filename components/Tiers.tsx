import React from 'react';
import { Check } from 'lucide-react';

const tiers = [
  {
    label: 'Tier 1',
    title: 'Utility API',
    highlight: false,
    features: [
      'Per-dispute pricing',
      'JSON-only output',
      'Rule ingestion support',
      'Basic audit logs',
    ],
  },
  {
    label: 'Tier 2',
    title: 'Review Dashboard',
    highlight: true,
    features: [
      'Web-based interface',
      'Human-in-the-loop workflows',
      'Visual case history',
      'Team management',
    ],
  },
  {
    label: 'Tier 3',
    title: 'Analytics & Audit',
    highlight: false,
    features: [
      'Consistency metrics',
      'Conflict trend analysis',
      'Compliance exports',
      'Dedicated support',
    ],
  },
];

export const Tiers: React.FC = () => {
  return (
    <section id="tiers" className="py-24 bg-ink-900/60 border-y border-white/5">
      <div className="container mx-auto px-6">
        <div className="text-center mb-12">
          <span className="text-teal-300 font-mono text-xs tracking-[0.3em] uppercase">Tiers</span>
          <h2 className="text-3xl md:text-4xl font-bold text-white mt-3">Product Tiers</h2>
          <p className="text-slate-400 mt-4 max-w-2xl mx-auto">
            Flexible integrations for platforms of any size, from API-first to full operations.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          {tiers.map((tier) => (
            <div
              key={tier.title}
              className={`rounded-2xl p-6 border transition-all ${
                tier.highlight
                  ? 'border-teal-400/70 bg-ink-950 shadow-xl shadow-teal-500/10'
                  : 'border-slate-800 bg-ink-900/70 hover:border-teal-400/30'
              }`}
            >
              <div className="text-xs uppercase tracking-[0.2em] text-slate-500">{tier.label}</div>
              <h3 className="text-2xl font-semibold text-white mt-3 mb-4">{tier.title}</h3>
              <ul className="space-y-3 text-sm text-slate-300">
                {tier.features.map((feature) => (
                  <li key={feature} className="flex items-start gap-3">
                    <span className="mt-0.5 w-5 h-5 rounded-full bg-teal-500/10 flex items-center justify-center">
                      <Check className="w-3 h-3 text-teal-300" />
                    </span>
                    {feature}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
