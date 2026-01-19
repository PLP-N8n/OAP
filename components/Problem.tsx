import React from 'react';
import { AlertTriangle, TrendingUp, Gavel } from 'lucide-react';

export const Problem: React.FC = () => {
  return (
    <section className="py-24 bg-slate-900/50 border-y border-white/5">
      <div className="container mx-auto px-6">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl md:text-4xl font-bold text-white mb-16 text-center">
            "Why did you ban me?"
          </h2>
          
          <div className="grid md:grid-cols-3 gap-8">
            <div className="glass-panel p-8 rounded-2xl">
              <div className="w-12 h-12 bg-red-500/10 rounded-lg flex items-center justify-center mb-6">
                <Gavel className="w-6 h-6 text-red-400" />
              </div>
              <h3 className="text-xl font-semibold text-white mb-3">Regulatory Panic</h3>
              <p className="text-slate-400 leading-relaxed">
                New regulations (EU DSA Art. 17) require you to provide specific reasoning for every moderation decision.
              </p>
            </div>
            
            <div className="glass-panel p-8 rounded-2xl">
              <div className="w-12 h-12 bg-orange-500/10 rounded-lg flex items-center justify-center mb-6">
                <TrendingUp className="w-6 h-6 text-orange-400" />
              </div>
              <h3 className="text-xl font-semibold text-white mb-3">Human Bottlenecks</h3>
              <p className="text-slate-400 leading-relaxed">
                Human moderators are too slow to write detailed legal justifications for millions of actions.
              </p>
            </div>
            
            <div className="glass-panel p-8 rounded-2xl">
              <div className="w-12 h-12 bg-yellow-500/10 rounded-lg flex items-center justify-center mb-6">
                <AlertTriangle className="w-6 h-6 text-yellow-400" />
              </div>
              <h3 className="text-xl font-semibold text-white mb-3">Black Box Risk</h3>
              <p className="text-slate-400 leading-relaxed">
                Standard AI "black boxes" are legally dangerous because they guess rather than cite.
              </p>
            </div>
          </div>

          <div className="mt-16 p-6 rounded-xl bg-red-500/5 border border-red-500/20 text-center">
             <p className="text-red-200 font-medium">
               <span className="font-bold text-red-400">THE RISK:</span> A single regulatory audit failure can cost <span className="underline decoration-red-500/50 decoration-2">6% of your global turnover</span>.
             </p>
          </div>
        </div>
      </div>
    </section>
  );
};