import React from 'react';
import { ArrowRight, ShieldCheck } from 'lucide-react';

export const Hero: React.FC = () => {
  return (
    <section className="relative pt-32 pb-20 lg:pt-48 lg:pb-32 overflow-hidden">
      <div className="absolute -top-32 right-12 w-[520px] h-[520px] bg-teal-500/20 rounded-full blur-[120px] float-slow -z-10" />
      <div className="absolute top-40 -left-32 w-[420px] h-[420px] bg-sky-500/10 rounded-full blur-[120px] -z-10" />

      <div className="container mx-auto px-6">
        <div className="grid lg:grid-cols-[1.1fr_0.9fr] gap-14 items-center">
          <div className="space-y-8">
            <div className="inline-flex items-center gap-2 bg-teal-500/10 border border-teal-400/30 rounded-full px-4 py-1.5 reveal">
              <ShieldCheck className="w-4 h-4 text-teal-300" />
              <span className="text-xs font-semibold tracking-[0.2em] uppercase text-teal-200">Article 17 Ready</span>
            </div>

            <h1 className="font-display text-5xl md:text-6xl lg:text-7xl font-semibold tracking-tight text-white leading-[1.05] reveal reveal-delay-1">
              Automate defensible moderation with
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-teal-300 via-sky-300 to-amber-300"> citation-anchored</span> adjudication.
            </h1>

            <p className="text-lg md:text-xl text-slate-300 max-w-2xl reveal reveal-delay-2">
              OAP turns messy community guidelines into structured legal reasoning. Every decision is traced to a specific rule clause before the verdict can ship.
            </p>

            <div className="flex flex-col sm:flex-row items-center gap-4 reveal reveal-delay-3">
              <a
                href="/protocol"
                className="w-full sm:w-auto px-8 py-4 bg-[color:var(--accent)] hover:bg-[color:var(--accent-strong)] text-ink-950 font-semibold rounded-lg transition-all shadow-lg shadow-teal-600/30 flex items-center justify-center group"
              >
                Read the Protocol
                <ArrowRight className="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform" />
              </a>

              <a
                href="#get-certified"
                className="w-full sm:w-auto px-8 py-4 glass-button text-slate-200 font-semibold rounded-lg hover:text-white transition-all text-center relative group"
              >
                Get Certified
                <span className="pointer-events-none absolute left-1/2 top-full mt-2 -translate-x-1/2 translate-y-1 whitespace-nowrap rounded-md border border-white/10 bg-ink-900/90 px-3 py-1 text-[10px] uppercase tracking-[0.2em] text-slate-200 opacity-0 transition group-hover:translate-y-0 group-hover:opacity-100 group-focus:translate-y-0 group-focus:opacity-100">
                  Coming soon
                </span>
              </a>
            </div>

            <div className="grid sm:grid-cols-3 gap-4 text-sm text-slate-300">
              <div className="glass-panel rounded-xl px-4 py-3">
                <span className="block text-white font-semibold">Zero hallucinations</span>
                <span className="text-slate-400">Verdicts require evidence.</span>
              </div>
              <div className="glass-panel rounded-xl px-4 py-3">
                <span className="block text-white font-semibold">Audit-ready in seconds</span>
                <span className="text-slate-400">Structured JSON output.</span>
              </div>
              <div className="glass-panel rounded-xl px-4 py-3">
                <span className="block text-white font-semibold">Policy-native</span>
                <span className="text-slate-400">No rule rewrites needed.</span>
              </div>
            </div>
          </div>

          <div className="relative">
            <div className="glass-panel rounded-2xl p-1 border border-teal-400/30 shadow-2xl shadow-teal-600/20">
              <div className="bg-ink-900/80 rounded-2xl p-6">
                <div className="flex items-center justify-between text-xs uppercase tracking-[0.2em] text-slate-400">
                  <span>Decision Packet</span>
                  <span className="text-teal-300">Live</span>
                </div>
                <div className="mt-6 space-y-4 font-mono text-sm text-slate-200">
                  <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                    <span className="text-slate-400">Rulebook</span>
                    <span className="text-sky-300">Community Policy v3.2</span>
                  </div>
                  <div>
                    <span className="text-slate-400">Citation</span>
                    <p className="mt-2 text-teal-200">Section 4.2: No sharing of private identifiers without consent.</p>
                  </div>
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <span className="text-slate-400">Verdict</span>
                      <p className="mt-2 text-amber-300 font-semibold">Violation</p>
                    </div>
                    <div>
                      <span className="text-slate-400">Confidence</span>
                      <p className="mt-2 text-sky-300 font-semibold">0.98</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div className="absolute -bottom-6 -left-6 glass-panel bg-ink-900/80 px-5 py-4 rounded-xl border border-amber-400/30 shadow-2xl">
              <div className="text-xs uppercase tracking-[0.25em] text-amber-200">Audit stamp</div>
              <div className="text-lg font-semibold text-white mt-1">Ready for regulators</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};
