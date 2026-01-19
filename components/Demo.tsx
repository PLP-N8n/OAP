import React, { useState } from 'react';
import { Play, Check, X } from 'lucide-react';
import { adjudicateContent } from '../services/geminiService';
import { DemoState } from '../types';

const DEFAULT_RULEBOOK = `1. Hate Speech: We do not allow content that attacks people based on race, ethnicity, or religion.
2. Harassment: You may not repeatedly target a user with unwanted messages.
3. Privacy: You may not post someone else's phone number or address (doxing).`;

const DEFAULT_CONTENT = `Hey everyone, look at this loser! His phone number is 555-0199, let's call him all night!`;

export const Demo: React.FC = () => {
  const [state, setState] = useState<DemoState>({
    rulebook: DEFAULT_RULEBOOK,
    content: DEFAULT_CONTENT,
    isLoading: false,
    result: null,
    error: null,
  });

  const handleRun = async () => {
    setState(s => ({ ...s, isLoading: true, result: null, error: null }));
    try {
      const result = await adjudicateContent(state.rulebook, state.content);
      setState(s => ({ ...s, isLoading: false, result }));
    } catch (err) {
      setState(s => ({ ...s, isLoading: false, error: "Failed to connect to OAP Engine. Please try again." }));
    }
  };

  return (
    <section id="demo" className="py-24 bg-ink-900/60 relative">
      <div className="container mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="font-display text-3xl md:text-4xl font-semibold text-white">Test the protocol live</h2>
          <p className="text-slate-400 mt-4 max-w-2xl mx-auto">
            Change the content, rerun the engine, and watch the citation anchor enforce evidence.
          </p>
        </div>

        <div className="grid lg:grid-cols-2 gap-8 max-w-6xl mx-auto">
          <div className="space-y-6">
            <div className="glass-panel p-6 rounded-xl">
              <label className="block text-xs font-semibold text-slate-300 mb-3 uppercase tracking-[0.3em]">Step 1: Rulebook</label>
              <textarea
                className="w-full h-44 bg-ink-950/60 border border-slate-700 rounded-lg p-4 text-slate-200 focus:ring-2 focus:ring-teal-400/70 focus:outline-none font-mono text-sm resize-none"
                value={state.rulebook}
                onChange={(e) => setState(s => ({ ...s, rulebook: e.target.value }))}
              />
            </div>

            <div className="glass-panel p-6 rounded-xl">
              <label className="block text-xs font-semibold text-slate-300 mb-3 uppercase tracking-[0.3em]">Step 2: Content</label>
              <textarea
                className="w-full h-28 bg-ink-950/60 border border-slate-700 rounded-lg p-4 text-slate-200 focus:ring-2 focus:ring-teal-400/70 focus:outline-none font-mono text-sm resize-none"
                value={state.content}
                onChange={(e) => setState(s => ({ ...s, content: e.target.value }))}
              />
            </div>

            <button
              onClick={handleRun}
              disabled={state.isLoading}
              className="w-full py-4 bg-[color:var(--accent)] hover:bg-[color:var(--accent-strong)] disabled:bg-teal-700/40 disabled:cursor-not-allowed text-ink-950 font-bold rounded-xl transition-all shadow-lg shadow-teal-900/20 flex items-center justify-center gap-2"
            >
              {state.isLoading ? (
                <div className="w-5 h-5 border-2 border-ink-950/40 border-t-ink-950 rounded-full animate-spin" />
              ) : (
                <>
                  <Play className="w-5 h-5 fill-current" />
                  Run Adjudication Protocol
                </>
              )}
            </button>
          </div>

          <div className="glass-panel rounded-xl p-1 relative min-h-[420px] flex flex-col">
            <div className="bg-ink-950/80 rounded-lg flex-1 p-8 font-mono relative overflow-hidden">
              <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-teal-400 via-sky-400 to-amber-300 opacity-60" />

              {!state.result && !state.isLoading && !state.error && (
                <div className="h-full flex flex-col items-center justify-center text-slate-500">
                  <div className="w-16 h-16 border-2 border-dashed border-slate-700 rounded-full flex items-center justify-center mb-4">
                    <Play className="w-6 h-6 ml-1 opacity-50" />
                  </div>
                  <p>Waiting for input stream...</p>
                </div>
              )}

              {state.error && (
                <div className="text-rose-300 p-4 border border-rose-500/20 bg-rose-500/10 rounded">
                  {state.error}
                </div>
              )}

              {state.result && (
                <div className="space-y-6 reveal">
                  <div className="border-b border-slate-800 pb-4">
                    <span className="text-slate-500 text-xs uppercase block mb-1">Verdict</span>
                    <div className="flex items-center gap-3">
                      {state.result.verdict === 'VIOLATION' ? (
                        <div className="flex items-center text-rose-300 gap-2">
                          <X className="w-6 h-6" />
                          <span className="text-2xl font-semibold">VIOLATION FOUND</span>
                        </div>
                      ) : (
                        <div className="flex items-center text-teal-300 gap-2">
                          <Check className="w-6 h-6" />
                          <span className="text-2xl font-semibold">NO VIOLATION</span>
                        </div>
                      )}
                    </div>
                  </div>

                  <div>
                    <span className="text-slate-500 text-xs uppercase block mb-2">Citation Anchor</span>
                    <div className="bg-teal-500/10 border-l-2 border-teal-400 p-4 text-teal-100 italic">
                      {state.result.citation ? `"${state.result.citation}"` : "N/A - No matching rule found."}
                    </div>
                  </div>

                  <div>
                    <span className="text-slate-500 text-xs uppercase block mb-2">Statement of Reasons</span>
                    <p className="text-slate-300 leading-relaxed">
                      {state.result.reasoning}
                    </p>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};
