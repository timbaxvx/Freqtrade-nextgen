import React from "react";

export default function Onboarding() {
  return (
    <div className="min-h-screen bg-bg-dark text-white p-8">
      <h1 className="text-2xl font-bold text-neon-cyan mb-4">Onboarding Tutorial</h1>
      <div className="bg-glass rounded-xl p-6 shadow-neon-cyan backdrop-blur-xs">
        <h2 className="text-xl font-semibold mb-4 text-neon-cyan">Welcome to Freqtrade NextGen!</h2>
        <p className="mb-4">This tutorial will guide you through the key features of the platform.</p>
        
        <h3 className="text-lg font-semibold text-neon-magenta mb-2">Step 1: Connect Your Exchange Account</h3>
        <p className="mb-4">Navigate to the <a href="/integrations" className="text-neon-lime hover:underline">Integrations</a> page to connect your Bybit or Binance account.</p>

        <h3 className="text-lg font-semibold text-neon-magenta mb-2">Step 2: Create Your First Bot</h3>
        <p className="mb-4">Go to the <a href="/bots" className="text-neon-lime hover:underline">Bots</a> page and click on "Create New Bot" to set up your automated trading.</p>

        <h3 className="text-lg font-semibold text-neon-magenta mb-2">Step 3: Explore Strategies</h3>
        <p className="mb-4">Visit the <a href="/strategies" className="text-neon-lime hover:underline">Strategies</a> page to discover pre-built strategies or create your own using the Visual Strategy Builder.</p>

        <h3 className="text-lg font-semibold text-neon-magenta mb-2">Step 4: Analyze Your Performance</h3>
        <p className="mb-4">Check your trading performance and portfolio analytics on the <a href="/analytics" className="text-neon-lime hover:underline">Analytics</a> page.</p>

        <h3 className="text-lg font-semibold text-neon-magenta mb-2">Step 5: Get AI Assistance</h3>
        <p className="mb-4">Use the <a href="/assistant" className="text-neon-lime hover:underline">AI Assistant</a> for trading insights and support.</p>

        <p className="mt-6">Enjoy your journey with Freqtrade NextGen!</p>
      </div>
    </div>
  );
}