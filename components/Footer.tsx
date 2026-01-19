import React from 'react';

export const Footer: React.FC = () => {
  return (
    <footer id="get-certified" className="bg-ink-950 pt-20 pb-10 border-t border-white/5">
      <div className="container mx-auto px-6 text-center">
        <div className="max-w-2xl mx-auto mb-20">
          <span className="text-xs uppercase tracking-[0.3em] text-slate-400">Ready to deploy</span>
          <h2 className="font-display text-4xl md:text-5xl font-semibold text-white mt-4 mb-6">
            Stop risking fines. Start automating trust.
          </h2>
          <button className="px-10 py-5 bg-gradient-to-r from-teal-400 via-sky-400 to-amber-300 hover:from-teal-300 hover:via-sky-300 hover:to-amber-200 text-ink-950 text-lg font-bold rounded-xl shadow-xl shadow-teal-900/20 transition-all transform hover:-translate-y-1">
            Get OAP Certified
          </button>
        </div>

        <div className="flex flex-col md:flex-row justify-between items-center text-slate-500 text-sm border-t border-white/5 pt-8">
          <div className="mb-4 md:mb-0">
            &copy; {new Date().getFullYear()} Open Adjudication Protocol. All rights reserved.
          </div>
          <div className="flex space-x-6">
            <a href="#" className="hover:text-white transition-colors">Privacy Policy</a>
            <a href="#" className="hover:text-white transition-colors">Terms of Service</a>
            <a href="#" className="hover:text-white transition-colors">GDPR Compliance</a>
          </div>
        </div>
      </div>
    </footer>
  );
};
