import React from 'react';
import { Eye, Scale, ShieldCheck, FileSearch } from 'lucide-react';

export const Problem: React.FC = () => {
  return (
    <section id="protocol" className="py-24 bg-ink-900/60 border-y border-white/5">
      <div className="container mx-auto px-6">
        <div className="max-w-5xl mx-auto">
          <div className="text-center mb-16">
            <span className="text-xs uppercase tracking-[0.3em] text-slate-400">Read the Protocol</span>
            <h2 className="font-display text-3xl md:text-4xl font-semibold text-white mt-4">
              Doctrine-Driven Adjudication
            </h2>
            <p className="text-slate-400 mt-4 max-w-2xl mx-auto">
              OAP shifts platforms from enforcement to adjudication, closing the legibility gap between
              automated detection and human explanation. It produces DSA Article 17-ready Statements of
              Reasons with exact rule citations.
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div className="glass-panel p-6 rounded-2xl border border-white/5 transition-all duration-300 hover:-translate-y-1 hover:border-teal-400/30">
              <div className="w-12 h-12 bg-teal-500/10 rounded-lg flex items-center justify-center mb-6">
                <Eye className="w-6 h-6 text-teal-300" />
              </div>
              <h3 className="text-lg font-semibold text-white mb-3">Radical Visibility</h3>
              <p className="text-slate-400 leading-relaxed">
                Reasoning is visible by default. Any redaction is disclosed and justified in-system.
              </p>
            </div>

            <div className="glass-panel p-6 rounded-2xl border border-white/5 transition-all duration-300 hover:-translate-y-1 hover:border-sky-400/30">
              <div className="w-12 h-12 bg-sky-500/10 rounded-lg flex items-center justify-center mb-6">
                <Scale className="w-6 h-6 text-sky-300" />
              </div>
              <h3 className="text-lg font-semibold text-white mb-3">Whiteboard Mandate</h3>
              <p className="text-slate-400 leading-relaxed">
                OAP illuminates disputes, mapping a resolution space without issuing verdicts.
              </p>
            </div>

            <div className="glass-panel p-6 rounded-2xl border border-white/5 transition-all duration-300 hover:-translate-y-1 hover:border-amber-400/30">
              <div className="w-12 h-12 bg-amber-500/10 rounded-lg flex items-center justify-center mb-6">
                <ShieldCheck className="w-6 h-6 text-amber-300" />
              </div>
              <h3 className="text-lg font-semibold text-white mb-3">Epistemic Humility</h3>
              <p className="text-slate-400 leading-relaxed">
                Uncertainty is explicit. Missing context is flagged, and the system refuses to guess.
              </p>
            </div>

            <div className="glass-panel p-6 rounded-2xl border border-white/5 transition-all duration-300 hover:-translate-y-1 hover:border-rose-400/30">
              <div className="w-12 h-12 bg-rose-500/10 rounded-lg flex items-center justify-center mb-6">
                <FileSearch className="w-6 h-6 text-rose-300" />
              </div>
              <h3 className="text-lg font-semibold text-white mb-3">Citation Anchoring</h3>
              <p className="text-slate-400 leading-relaxed">
                Every evaluative statement must quote an exact, platform-supplied rule clause.
              </p>
            </div>
          </div>

          <div className="mt-16 p-6 rounded-2xl bg-ink-950/80 border border-white/5">
            <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-6">
              <div className="max-w-xl">
                <span className="text-teal-300 tracking-[0.2em] text-xs uppercase">DSA Ready</span>
                <h4 className="text-lg font-semibold text-white mt-2">Statements of Reasons, at scale.</h4>
                <p className="text-slate-300 mt-3">
                  OAP outputs structured JSON with neutral summaries, exact rule citations, ambiguity flags,
                  and automated-means disclosure required for Article 17 compliance.
                </p>
              </div>
              <div className="grid grid-cols-2 gap-x-6 gap-y-3 text-sm text-slate-300">
                <span className="flex items-center gap-2">
                  <span className="w-2 h-2 bg-teal-400/80 rounded-full"></span>
                  Facts and context
                </span>
                <span className="flex items-center gap-2">
                  <span className="w-2 h-2 bg-sky-400/80 rounded-full"></span>
                  Exact rule clause
                </span>
                <span className="flex items-center gap-2">
                  <span className="w-2 h-2 bg-amber-400/80 rounded-full"></span>
                  Automated means
                </span>
                <span className="flex items-center gap-2">
                  <span className="w-2 h-2 bg-rose-400/80 rounded-full"></span>
                  Resolution space
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};
