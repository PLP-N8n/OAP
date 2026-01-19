import React from 'react';
import { Lock, FileText, CheckCircle2 } from 'lucide-react';

export const Solution: React.FC = () => {
  return (
    <section id="integration" className="py-24 relative overflow-hidden">
      <div className="absolute right-0 top-1/2 -translate-y-1/2 w-[620px] h-[620px] bg-teal-500/10 rounded-full blur-[100px] -z-10" />

      <div className="container mx-auto px-6">
        <div className="flex flex-col lg:flex-row items-center gap-16">
          <div className="lg:w-1/2">
            <span className="text-xs uppercase tracking-[0.3em] text-slate-400">The Protocol</span>
            <h2 className="font-display text-3xl md:text-5xl font-semibold text-white mt-4 mb-6">
              The first citation-anchored governance engine.
            </h2>
            <p className="text-xl text-slate-300 mb-8">
              OAP is not a chatbot. It is a procedural protocol that refuses to decide without evidence.
            </p>

            <div className="space-y-6">
              <div className="flex items-start">
                <div className="flex-shrink-0 w-9 h-9 rounded-full bg-teal-500/15 flex items-center justify-center mt-1">
                  <Lock className="w-4 h-4 text-teal-300" />
                </div>
                <div className="ml-4">
                  <h4 className="text-lg font-semibold text-white">The Safety Gate</h4>
                  <p className="text-slate-400 mt-2">
                    The engine is architecturally forbidden from issuing a verdict unless it can quote the exact rule clause that was violated.
                  </p>
                </div>
              </div>

              <div className="flex items-start">
                <div className="flex-shrink-0 w-9 h-9 rounded-full bg-amber-500/15 flex items-center justify-center mt-1">
                  <CheckCircle2 className="w-4 h-4 text-amber-300" />
                </div>
                <div className="ml-4">
                  <h4 className="text-lg font-semibold text-white">The Result</h4>
                  <p className="text-slate-400 mt-2">
                    Audit-ready decisions with a structured Statement of Reasons, ready for regulators and appeals.
                  </p>
                </div>
              </div>
            </div>
          </div>

          <div className="lg:w-1/2 relative">
            <div className="glass-panel rounded-2xl border border-teal-400/30 p-1 shadow-2xl shadow-teal-600/20">
              <div className="bg-ink-900/90 rounded-xl p-6 font-mono text-sm space-y-4">
                <div className="flex items-center space-x-2 text-slate-500 mb-4 border-b border-slate-800 pb-2">
                  <FileText className="w-4 h-4" />
                  <span>audit_log_28491.json</span>
                </div>
                <div>
                  <span className="text-teal-300">"verdict"</span>: <span className="text-rose-300">"VIOLATION"</span>,
                </div>
                <div>
                  <span className="text-teal-300">"citation_anchor"</span>: <span className="text-sky-300">"Section 4.2: Users may not share PII without consent."</span>,
                </div>
                <div>
                  <span className="text-teal-300">"confidence"</span>: <span className="text-amber-300">0.98</span>,
                </div>
                <div>
                  <span className="text-teal-300">"method"</span>: <span className="text-slate-300">"EXACT_MATCH_EXTRACTION"</span>
                </div>
              </div>
            </div>
            <div className="absolute -bottom-6 -right-6 glass-panel bg-ink-900/80 px-6 py-4 rounded-lg border border-teal-400/30 shadow-2xl">
              <div className="flex items-center gap-3">
                <div className="w-2.5 h-2.5 bg-teal-400 rounded-full animate-pulse"></div>
                <span className="text-teal-300 font-semibold">Audit Passed</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};
