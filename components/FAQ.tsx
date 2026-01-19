import React from 'react';
import { ChevronDown } from 'lucide-react';

export const FAQ: React.FC = () => {
  return (
    <section className="py-24 bg-slate-900/50">
      <div className="container mx-auto px-6 max-w-3xl">
        <h2 className="text-3xl font-bold text-white mb-12 text-center">Frequently Asked Questions</h2>
        
        <div className="space-y-4">
          <div className="glass-panel p-6 rounded-xl">
            <h3 className="text-lg font-semibold text-white mb-2">Will the AI hallucinate a rule?</h3>
            <p className="text-slate-400">
              No. OAP uses strict Citation Anchoring. If it cannot find a text match in your rules, it returns "No Violation Found" and escalates to a human. This "fail-safe" mode prevents legal liability.
            </p>
          </div>
          
          <div className="glass-panel p-6 rounded-xl">
            <h3 className="text-lg font-semibold text-white mb-2">Do I need to rewrite my guidelines?</h3>
            <p className="text-slate-400">
              No. Our Ingestion Engine normalizes your existing text for you, converting PDF/Docx policies into our semantic graph format automatically.
            </p>
          </div>

          <div className="glass-panel p-6 rounded-xl">
            <h3 className="text-lg font-semibold text-white mb-2">How does this help with the EU DSA?</h3>
            <p className="text-slate-400">
              Article 17 requires a "Statement of Reasons" for every moderation action. OAP generates this instantly using the exact language of your Terms of Service, meeting the transparency requirement at scale.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};