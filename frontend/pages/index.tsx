import React from "react";
import Link from "next/link";
import PortfolioChart from "../components/PortfolioChart";
import BotStatusGrid from "../components/BotStatusGrid";
import GPTAssistant from "../components/GPTAssistant";

export default function Home() {
  return (
    <div className="bg-bg-dark min-h-screen text-white">
      <main className="p-8 grid grid-cols-3 gap-8">
        <section className="col-span-2 bg-glass rounded-xl p-6 shadow-neon-cyan backdrop-blur-xs">
          <h2 className="text-xl font-semibold mb-4 text-neon-cyan">Portfolio</h2>
          <PortfolioChart />
        </section>
        <aside className="bg-glass rounded-xl p-6 shadow-neon-magenta backdrop-blur-xs flex flex-col gap-4">
          <h2 className="text-xl font-semibold text-neon-magenta">GPT-4.1 Insights</h2>
          <GPTAssistant />
          <Link href="/strategy-builder">
            <button className="mt-4 bg-neon-cyan text-bg-dark font-bold py-2 rounded shadow-neon-cyan hover:bg-neon-lime transition">Strategie-Builder öffnen</button>
          </Link>
        </aside>
      </main>
      <footer className="p-4 text-center text-neon-magenta">© 2025 Freqtrade NextGen</footer>
    </div>
  );
}