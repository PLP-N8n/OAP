import React from 'react';
import { TrendingDown, Clock } from 'lucide-react';

export const Impact: React.FC = () => {
  return (
    <section id="impact" className="py-24 bg-ink-950">
      <div className="container mx-auto px-6">
        <div className="mb-12">
          <span className="text-teal-300 font-mono text-xs tracking-[0.3em] uppercase">Impact</span>
          <h2 className="text-3xl md:text-4xl font-bold text-white mt-3">
            Success Metrics & Proof
          </h2>
          <p className="text-slate-400 mt-4 max-w-2xl">
            Transparent reasoning reduces appeals and compresses resolution time by turning debate
            into verification.
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-8">
          <div className="glass-panel p-8 rounded-2xl">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 bg-teal-500/10 rounded-lg flex items-center justify-center">
                <TrendingDown className="w-5 h-5 text-teal-300" />
              </div>
              <div>
                <h3 className="text-lg font-semibold text-white">Reduction in User Appeals</h3>
                <p className="text-sm text-slate-400">Cited decisions are harder to dispute.</p>
              </div>
            </div>
            <div className="space-y-4">
              <div>
                <div className="flex items-center justify-between text-xs text-slate-400">
                  <span>Opaque moderation</span>
                  <span>25%</span>
                </div>
                <div className="h-2 bg-slate-800 rounded-full mt-2">
                  <div className="h-2 bg-slate-500 rounded-full" style={{ width: '25%' }} />
                </div>
              </div>
              <div>
                <div className="flex items-center justify-between text-xs text-slate-400">
                  <span>OAP with citations</span>
                  <span>8%</span>
                </div>
                <div className="h-2 bg-slate-800 rounded-full mt-2">
                  <div className="h-2 bg-teal-400 rounded-full" style={{ width: '8%' }} />
                </div>
              </div>
              <p className="text-sm text-slate-400">
                Clear statements of reasons cut appeal volume by ~60%.
              </p>
            </div>
          </div>

          <div className="glass-panel p-8 rounded-2xl">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 bg-amber-500/10 rounded-lg flex items-center justify-center">
                <Clock className="w-5 h-5 text-amber-400" />
              </div>
              <div>
                <h3 className="text-lg font-semibold text-white">Handling Time per Dispute</h3>
                <p className="text-sm text-slate-400">From investigation to verification.</p>
              </div>
            </div>
            <div className="space-y-4">
              <div>
                <div className="flex items-center justify-between text-xs text-slate-400">
                  <span>Manual review</span>
                  <span>15 min</span>
                </div>
                <div className="h-2 bg-slate-800 rounded-full mt-2">
                  <div className="h-2 bg-slate-500 rounded-full" style={{ width: '90%' }} />
                </div>
              </div>
              <div>
                <div className="flex items-center justify-between text-xs text-slate-400">
                  <span>OAP-assisted</span>
                  <span>2 min</span>
                </div>
                <div className="h-2 bg-slate-800 rounded-full mt-2">
                  <div className="h-2 bg-amber-500 rounded-full" style={{ width: '15%' }} />
                </div>
              </div>
              <p className="text-sm text-slate-400">
                AI drafts the statement, humans verify, and the case moves faster.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};
