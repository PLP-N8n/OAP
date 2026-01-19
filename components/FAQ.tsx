import React from 'react';

export const FAQ: React.FC = () => {
  return (
    <section id="compliance" className="py-24 bg-ink-900/50">
      <div className="container mx-auto px-6 max-w-4xl">
        <div className="text-center mb-12">
          <span className="text-xs uppercase tracking-[0.3em] text-slate-400">Compliance</span>
          <h2 className="font-display text-3xl md:text-4xl font-semibold text-white mt-4">Questions regulators will ask</h2>
          <p className="text-slate-400 mt-4">
            Clear answers for legal, policy, and trust teams.
          </p>
        </div>

        <div className="space-y-4">
          <div className="glass-panel p-6 rounded-2xl border border-white/5">
            <h3 className="text-lg font-semibold text-white mb-2">Will the AI hallucinate a rule?</h3>
            <p className="text-slate-400">
              No. OAP enforces citation anchoring. If it cannot match text in your rules, it returns "No Violation" and escalates to a human review queue.
            </p>
          </div>

          <div className="glass-panel p-6 rounded-2xl border border-white/5">
            <h3 className="text-lg font-semibold text-white mb-2">Do we need to rewrite our guidelines?</h3>
            <p className="text-slate-400">
              No. The ingestion engine normalizes existing text, including PDF or docx policies, into a structured rulebook.
            </p>
          </div>

          <div className="glass-panel p-6 rounded-2xl border border-white/5">
            <h3 className="text-lg font-semibold text-white mb-2">How does this satisfy EU DSA Article 17?</h3>
            <p className="text-slate-400">
              Article 17 requires a Statement of Reasons for every moderation action. OAP generates it instantly with exact rule citations.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};
