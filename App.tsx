import React, { useState, useEffect } from 'react';
import { ArrowUp } from 'lucide-react';
import { Hero } from './components/Hero';
import { Problem } from './components/Problem';
import { Solution } from './components/Solution';
import { HowItWorks } from './components/HowItWorks';
import { Demo } from './components/Demo';
import { FAQ } from './components/FAQ';
import { Footer } from './components/Footer';

const App: React.FC = () => {
  const [showScrollTop, setShowScrollTop] = useState(false);

  const scrollToCTA = () => {
    document.getElementById('get-certified')?.scrollIntoView({ behavior: 'smooth' });
  };

  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth',
    });
  };

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 300) {
        setShowScrollTop(true);
      } else {
        setShowScrollTop(false);
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <main className="min-h-screen bg-slate-950 text-white selection:bg-blue-500/30 relative">
        <nav className="fixed w-full z-50 glass-panel border-b border-white/5 bg-slate-950/80">
            <div className="container mx-auto px-6 h-16 flex items-center justify-between">
                <div className="font-bold text-xl tracking-tight text-white flex items-center gap-2">
                    <div className="w-6 h-6 bg-blue-500 rounded-md"></div>
                    OAP
                </div>
                <div className="hidden md:flex space-x-8 text-sm font-medium text-slate-300">
                    <a href="#" className="hover:text-white transition-colors">Protocol</a>
                    <a href="#" className="hover:text-white transition-colors">Integration</a>
                    <a href="#" className="hover:text-white transition-colors">Compliance</a>
                </div>
                <div className="flex items-center gap-4">
                    <button className="text-slate-400 hover:text-white text-sm font-medium transition-colors">
                        Login
                    </button>
                    <button 
                        onClick={scrollToCTA}
                        className="px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white text-sm font-semibold rounded-lg transition-all shadow-lg shadow-blue-600/20"
                    >
                        Get Certified
                    </button>
                </div>
            </div>
        </nav>
      <Hero />
      <Problem />
      <Solution />
      <Demo />
      <HowItWorks />
      <div className="py-12 bg-slate-950 border-y border-white/5">
        <div className="container mx-auto px-6 flex flex-wrap justify-center gap-6 md:gap-12 opacity-50 grayscale hover:grayscale-0 transition-all duration-500">
             {/* Simple text badges for "Standard" proof */}
             <span className="text-xl font-bold text-white flex items-center gap-2">🇪🇺 DSA Compliant Architecture</span>
             <span className="text-xl font-bold text-white flex items-center gap-2">🛡️ GDPR Safe</span>
             <span className="text-xl font-bold text-white flex items-center gap-2">🤝 Human-in-the-Loop</span>
        </div>
      </div>
      <FAQ />
      <Footer />

      {/* Scroll to Top Button */}
      <button
        onClick={scrollToTop}
        className={`fixed bottom-8 right-8 p-3 bg-slate-800/80 hover:bg-blue-600 backdrop-blur-md border border-slate-700 hover:border-blue-500 text-white rounded-lg shadow-xl transition-all duration-300 z-50 group ${
          showScrollTop ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10 pointer-events-none'
        }`}
        aria-label="Scroll to top"
      >
        <ArrowUp className="w-6 h-6 text-slate-400 group-hover:text-white transition-colors" />
      </button>
    </main>
  );
};

export default App;