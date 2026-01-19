import React, { useState } from 'react';
import { Play, ShieldCheck, MessageCircleWarning, FileText } from 'lucide-react';

type Doctrine = 'strict' | 'loose';
type Scenario = 'spam' | 'harassment';

type SimulationResult = {
  json: Record<string, unknown>;
  summary: string;
};

const scenarioLabels: Record<Scenario, { title: string; description: string }> = {
  spam: {
    title: 'Crypto Promotion',
    description: 'User posts referral link 5 times in 1 minute.',
  },
  harassment: {
    title: 'Heated Debate',
    description: 'User calls another user "ignorant" in a political thread.',
  },
};

const simulationMatrix: Record<Doctrine, Record<Scenario, SimulationResult>> = {
  strict: {
    spam: {
      json: {
        verdict: 'Violation',
        citation_anchor: {
          rule_id: 'rule_002',
          quoted_rule_text: 'No spam or repeated promotion links.',
        },
        reasoning: 'Content aligns with rule rule_002. Matched keywords: spam, promotion.',
        confidence: 0.91,
        flags: [],
        match_details: {
          exact_score: 0.67,
          semantic_score: 0.44,
        },
      },
      summary: 'Normalized rulebook anchors the anti-spam clause and returns a violation.',
    },
    harassment: {
      json: {
        verdict: 'Violation',
        citation_anchor: {
          rule_id: 'rule_001',
          quoted_rule_text: 'No harassment or personal attacks toward other users.',
        },
        reasoning: 'Content aligns with rule rule_001. Matched keywords: harassment, attacks.',
        confidence: 0.86,
        flags: [],
        match_details: {
          exact_score: 0.58,
          semantic_score: 0.39,
        },
      },
      summary: 'Strict doctrine anchors the civility rule and returns a violation.',
    },
  },
  loose: {
    spam: {
      json: {
        verdict: 'No Violation',
        citation_anchor: null,
        reasoning: 'No rule could be anchored to the content.',
        confidence: 0.21,
        flags: ['NO_APPLICABLE_RULE'],
      },
      summary: 'Permissive ruleset lacks a strict anti-spam clause, so no violation is anchored.',
    },
    harassment: {
      json: {
        verdict: 'No Violation',
        citation_anchor: null,
        reasoning: 'No rule could be anchored to the content.',
        confidence: 0.18,
        flags: ['NO_APPLICABLE_RULE'],
      },
      summary: 'Permissive doctrine protects debate and yields no anchored violation.',
    },
  },
};

export const Simulator: React.FC = () => {
  const [doctrine, setDoctrine] = useState<Doctrine>('strict');
  const [scenario, setScenario] = useState<Scenario>('spam');
  const [result, setResult] = useState<SimulationResult | null>(null);

  const runSimulation = () => {
    setResult(simulationMatrix[doctrine][scenario]);
  };

  return (
    <section id="simulator" className="py-24 bg-ink-900/60 border-y border-white/5">
      <div className="container mx-auto px-6">
        <div className="text-center mb-14">
          <span className="text-teal-300 font-mono text-xs tracking-[0.3em] uppercase">Simulator</span>
          <h2 className="text-3xl md:text-4xl font-bold text-white mt-3">
            The Adjudication Engine
          </h2>
          <p className="text-slate-400 max-w-2xl mx-auto mt-4">
            Normalize rulebooks with normalizer.py, then apply citation anchoring to disputes. This
            mirrors the local Python pipeline and returns the same JSON schema.
          </p>
        </div>

        <div className="grid lg:grid-cols-12 gap-8 items-start">
          <div className="lg:col-span-4 space-y-6">
            <div className="glass-panel p-6 rounded-2xl">
              <div className="flex items-center gap-3 mb-4">
                <div className="w-9 h-9 rounded-lg bg-teal-500/10 flex items-center justify-center">
                  <ShieldCheck className="w-5 h-5 text-teal-300" />
                </div>
                <div>
                  <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Doctrine</p>
                  <h3 className="text-lg font-semibold text-white">Select Rulebook Doctrine</h3>
                </div>
              </div>
              <div className="space-y-3">
                <button
                  type="button"
                  onClick={() => setDoctrine('strict')}
                  className={`w-full text-left p-4 rounded-xl border transition-all ${
                    doctrine === 'strict'
                      ? 'border-teal-400/70 bg-teal-500/10 text-white shadow-lg shadow-teal-500/10'
                      : 'border-slate-700 bg-ink-950/40 text-slate-300 hover:border-teal-400/40'
                  }`}
                >
                  <div className="font-semibold">Strict / Corporate</div>
                  <div className="text-xs text-slate-400 mt-1">
                    Zero tolerance, fast enforcement, strict safety.
                  </div>
                </button>
                <button
                  type="button"
                  onClick={() => setDoctrine('loose')}
                  className={`w-full text-left p-4 rounded-xl border transition-all ${
                    doctrine === 'loose'
                      ? 'border-sky-400/70 bg-sky-500/10 text-white shadow-lg shadow-sky-500/10'
                      : 'border-slate-700 bg-ink-950/40 text-slate-300 hover:border-sky-400/40'
                  }`}
                >
                  <div className="font-semibold">Permissive / Free Speech</div>
                  <div className="text-xs text-slate-400 mt-1">
                    Context heavy, high threshold for action.
                  </div>
                </button>
              </div>
            </div>

            <div className="glass-panel p-6 rounded-2xl">
              <div className="flex items-center gap-3 mb-4">
                <div className="w-9 h-9 rounded-lg bg-amber-500/10 flex items-center justify-center">
                  <MessageCircleWarning className="w-5 h-5 text-amber-400" />
                </div>
                <div>
                  <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Scenario</p>
                  <h3 className="text-lg font-semibold text-white">Select Dispute Event</h3>
                </div>
              </div>
              <div className="space-y-3">
                {(['spam', 'harassment'] as Scenario[]).map((item) => (
                  <button
                    key={item}
                    type="button"
                    onClick={() => setScenario(item)}
                    className={`w-full text-left p-4 rounded-xl border transition-all ${
                      scenario === item
                        ? 'border-amber-500/60 bg-amber-500/10 text-white shadow-lg shadow-amber-500/10'
                      : 'border-slate-700 bg-ink-950/40 text-slate-300 hover:border-amber-500/40'
                    }`}
                  >
                    <div className="font-semibold">{scenarioLabels[item].title}</div>
                    <div className="text-xs text-slate-400 mt-1">
                      {scenarioLabels[item].description}
                    </div>
                  </button>
                ))}
              </div>
            </div>

            <button
              type="button"
              onClick={runSimulation}
              className="w-full py-4 bg-[color:var(--accent)] hover:bg-[color:var(--accent-strong)] text-ink-950 font-semibold rounded-xl transition-all shadow-lg shadow-teal-600/30 flex items-center justify-center gap-2"
            >
              <Play className="w-5 h-5" />
              Adjudicate Event
            </button>
          </div>

          <div className="lg:col-span-8">
            <div className="glass-panel rounded-2xl overflow-hidden border border-slate-800/80">
              <div className="bg-ink-800/90 px-5 py-3 border-b border-slate-800 flex items-center justify-between">
                <div className="flex items-center gap-2 text-slate-400 text-xs uppercase tracking-[0.2em]">
                  <FileText className="w-4 h-4" />
                  Statement of Reasons
                </div>
                <div className="text-slate-500 text-xs">normalizer.py + citation_checker.py</div>
              </div>
              <div className="p-6 bg-ink-950/80 min-h-[360px]">
                {!result ? (
                  <div className="h-full flex flex-col items-center justify-center text-slate-500">
                    <div className="w-14 h-14 border border-dashed border-slate-700 rounded-full flex items-center justify-center mb-4">
                      <Play className="w-6 h-6" />
                    </div>
                    <p>Ready to process dispute.</p>
                    <p className="text-xs mt-2 text-slate-600">
                      Select options on the left and click Adjudicate.
                    </p>
                  </div>
                ) : (
                  <div className="space-y-6">
                    <div className="text-xs uppercase tracking-[0.2em] text-slate-500">Output JSON</div>
                    <pre className="text-sm text-slate-200 bg-ink-900/70 border border-slate-800 rounded-xl p-4 overflow-x-auto whitespace-pre-wrap">
                      {JSON.stringify(result.json, null, 2)}
                    </pre>
                    <div className="bg-ink-900/70 border border-slate-800 rounded-xl p-4">
                      <div className="text-xs uppercase tracking-[0.2em] text-teal-300 mb-2">
                        OAP Analysis
                      </div>
                      <p className="text-slate-200">{result.summary}</p>
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};
