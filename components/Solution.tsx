import React from 'react';
import { Lock, FileText, CheckCircle2 } from 'lucide-react';

export const Solution: React.FC = () => {
  return (
    <section className="py-24 relative overflow-hidden">
        {/* Decorative elements */}
        <div className="absolute right-0 top-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-cyan-500/5 rounded-full blur-[80px] -z-10" />

      <div className="container mx-auto px-6">
        <div className="flex flex-col lg:flex-row items-center gap-16">
          <div className="lg:w-1/2">
            <h2 className="text-3xl md:text-5xl font-bold text-white mb-6">
              The First "Citation-Anchored" Governance Engine.
            </h2>
            <p className="text-xl text-slate-400 mb-8 font-light">
              OAP is not a chatbot. It is a rigid procedural protocol.
            </p>
            
            <div className="space-y-6">
              <div className="flex items-start">
                <div className="flex-shrink-0 w-8 h-8 rounded-full bg-blue-500/20 flex items-center justify-center mt-1">
                  <Lock className="w-4 h-4 text-blue-400" />
                </div>
                <div className="ml-4">
                  <h4 className="text-lg font-semibold text-white">The Safety Gate</h4>
                  <p className="text-slate-400 mt-2">
                    Our AI is architecturally forbidden from issuing a verdict unless it can extract and quote the <span className="text-blue-300 italic">exact clause</span> from your rulebook that was violated.
                  </p>
                </div>
              </div>
              
              <div className="flex items-start">
                <div className="flex-shrink-0 w-8 h-8 rounded-full bg-green-500/20 flex items-center justify-center mt-1">
                  <CheckCircle2 className="w-4 h-4 text-green-400" />
                </div>
                <div className="ml-4">
                  <h4 className="text-lg font-semibold text-white">The Result</h4>
                  <p className="text-slate-400 mt-2">
                    100% Audit-Ready, Defensible transparency. No guessing. No hallucinating.
                  </p>
                </div>
              </div>
            </div>
          </div>
          
          <div className="lg:w-1/2 relative">
            <div className="glass-panel rounded-xl border border-blue-500/30 p-1">
                <div className="bg-slate-900/90 rounded-lg p-6 font-mono text-sm space-y-4">
                    <div className="flex items-center space-x-2 text-slate-500 mb-4 border-b border-slate-800 pb-2">
                        <FileText className="w-4 h-4" />
                        <span>audit_log_28491.json</span>
                    </div>
                    <div>
                        <span className="text-purple-400">"verdict"</span>: <span className="text-red-400">"VIOLATION"</span>,
                    </div>
                    <div>
                        <span className="text-purple-400">"citation_anchor"</span>: <span className="text-green-400">"Section 4.2: Users may not share PII of others without consent."</span>,
                    </div>
                    <div>
                         <span className="text-purple-400">"confidence"</span>: <span className="text-blue-400">1.0</span>,
                    </div>
                    <div>
                        <span className="text-purple-400">"method"</span>: <span className="text-yellow-400">"EXACT_MATCH_EXTRACTION"</span>
                    </div>
                </div>
            </div>
            {/* Floating badge */}
            <div className="absolute -bottom-6 -right-6 glass-panel bg-slate-900/80 px-6 py-4 rounded-lg border border-green-500/30 shadow-2xl">
                 <div className="flex items-center gap-3">
                     <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
                     <span className="text-green-400 font-semibold">Audit Passed</span>
                 </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};