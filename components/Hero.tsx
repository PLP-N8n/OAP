import React from 'react';
import { ArrowRight, ShieldCheck } from 'lucide-react';

export const Hero: React.FC = () => {
  return (
    <section className="relative pt-32 pb-20 lg:pt-48 lg:pb-32 overflow-hidden">
      {/* Background Glows */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-blue-500/20 rounded-full blur-[100px] -z-10" />
      
      <div className="container mx-auto px-6 text-center max-w-5xl">
        <div className="inline-flex items-center space-x-2 bg-blue-500/10 border border-blue-500/20 rounded-full px-4 py-1.5 mb-8">
          <ShieldCheck className="w-4 h-4 text-blue-400" />
          <span className="text-sm font-medium text-blue-300">EU DSA Article 17 Ready</span>
        </div>
        
        <h1 className="text-5xl md:text-7xl font-bold tracking-tight text-white mb-8 leading-[1.1]">
          Automate DSA Compliance with <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300">Hallucination-Free</span> Adjudication.
        </h1>
        
        <p className="text-xl md:text-2xl text-slate-400 mb-12 max-w-3xl mx-auto font-light">
          The Open Adjudication Protocol (OAP) turns your messy Community Guidelines into precise, legally defensible "Statements of Reasons"—instantly.
        </p>
        
        <div className="flex flex-col sm:flex-row items-center justify-center space-y-4 sm:space-y-0 sm:space-x-6">
          <button className="w-full sm:w-auto px-8 py-4 bg-blue-600 hover:bg-blue-500 text-white font-semibold rounded-lg transition-all shadow-lg shadow-blue-600/20 flex items-center justify-center group">
            Get Certified
            <ArrowRight className="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform" />
          </button>
          
          <button className="w-full sm:w-auto px-8 py-4 glass-button text-slate-300 font-medium rounded-lg hover:text-white transition-all">
            Read the Protocol
          </button>
        </div>
      </div>
    </section>
  );
};