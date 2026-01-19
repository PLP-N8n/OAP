import React, { useState, useEffect } from 'react';
import { ArrowUp, Scale, ShieldCheck, Users } from 'lucide-react';
import { Hero } from './components/Hero';
import { Problem } from './components/Problem';
import { Solution } from './components/Solution';
import { Simulator } from './components/Simulator';
import { Impact } from './components/Impact';
import { HowItWorks } from './components/HowItWorks';
import { Tiers } from './components/Tiers';
import { Risks } from './components/Risks';
import { FAQ } from './components/FAQ';
import { Footer } from './components/Footer';
import { Whitepaper } from './components/Whitepaper';

const App: React.FC = () => {
  const [showScrollTop, setShowScrollTop] = useState(false);
  const isProtocolPage = typeof window !== 'undefined'
    && window.location.pathname.toLowerCase() === '/protocol';

  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth',
    });
  };

  useEffect(() => {
    if (isProtocolPage) {
      setShowScrollTop(false);
      return;
    }

    const handleScroll = () => {
      if (window.scrollY > 300) {
        setShowScrollTop(true);
      } else {
        setShowScrollTop(false);
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, [isProtocolPage]);

  if (isProtocolPage) {
    return <Whitepaper />;
  }

  return (
    <main className="min-h-screen text-white selection:bg-teal-400/20 relative">
      <nav className="fixed w-full z-50 border-b border-white/5 bg-ink-900/80 backdrop-blur-xl">
        <div className="container mx-auto px-6 h-16 flex items-center justify-between">
          <div className="font-display font-semibold text-xl tracking-tight text-white flex items-center gap-3">
            <div className="w-7 h-7 rounded-md bg-gradient-to-br from-teal-400 via-sky-400 to-amber-400 shadow-lg shadow-teal-500/30"></div>
            <span className="md:hidden">OAP</span>
            <span className="hidden md:inline">Open Adjudication Protocol</span>
          </div>
          <div className="hidden md:flex items-center space-x-6 text-sm font-semibold text-slate-300">
            <a href="#simulator" className="hover:text-white transition-colors">Simulator</a>
            <a href="#impact" className="hover:text-white transition-colors">Impact</a>
            <a href="#tiers" className="hover:text-white transition-colors">Tiers</a>
            <a href="#risks" className="hover:text-white transition-colors">Risks</a>
          </div>
          <div className="flex items-center gap-4">
            <button className="text-slate-400 hover:text-white text-sm font-medium transition-colors">
              Login
            </button>
            <a
              href="/protocol"
              className="px-4 py-2 bg-[color:var(--accent)] hover:bg-[color:var(--accent-strong)] text-ink-950 text-sm font-semibold rounded-lg transition-all shadow-lg shadow-teal-600/30"
            >
              Read the Protocol
            </a>
          </div>
        </div>
      </nav>
      <Hero />
      <Problem />
      <Solution />
      <Simulator />
      <Impact />
      <HowItWorks />
      <Tiers />
      <div className="py-12 bg-ink-950 border-y border-white/5">
        <div className="container mx-auto px-6 flex flex-wrap justify-center gap-6 md:gap-10 text-slate-300">
          <div className="glass-panel px-5 py-3 rounded-full flex items-center gap-3">
            <Scale className="w-4 h-4 text-teal-300" />
            <span className="text-sm font-semibold tracking-wide uppercase">DSA Ready Architecture</span>
          </div>
          <div className="glass-panel px-5 py-3 rounded-full flex items-center gap-3">
            <ShieldCheck className="w-4 h-4 text-sky-300" />
            <span className="text-sm font-semibold tracking-wide uppercase">GDPR Safe by Design</span>
          </div>
          <div className="glass-panel px-5 py-3 rounded-full flex items-center gap-3">
            <Users className="w-4 h-4 text-amber-300" />
            <span className="text-sm font-semibold tracking-wide uppercase">Human-in-the-Loop</span>
          </div>
        </div>
      </div>
      <Risks />
      <FAQ />
      <Footer />

      {/* Scroll to Top Button */}
      <button
        onClick={scrollToTop}
        className={`fixed bottom-8 right-8 p-3 bg-ink-800/80 hover:bg-[color:var(--accent)] backdrop-blur-md border border-slate-700/60 hover:border-teal-400 text-white rounded-lg shadow-xl transition-all duration-300 z-50 group ${
          showScrollTop ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10 pointer-events-none'
        }`}
        aria-label="Scroll to top"
      >
        <ArrowUp className="w-6 h-6 text-slate-300 group-hover:text-ink-950 transition-colors" />
      </button>
    </main>
  );
};

export default App;
