import React, { useEffect, useState } from "react";
import { Strategy } from "../../shared/types";

export default function Strategies() {
  const [strategies, setStrategies] = useState<Strategy[]>([]);

  useEffect(() => {
    // Fetch strategies from backend
    const fetchStrategies = async () => {
      try {
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/strategies`, {
          headers: {
            'Authorization': 'Bearer YOUR_AUTH_TOKEN' // Replace with actual token
          }
        });
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data: Strategy[] = await response.json();
        setStrategies(data);
      } catch (error) {
        console.error("Error fetching strategies:", error);
      }
    };
    fetchStrategies();
  }, []);

  return (
    <div className="min-h-screen bg-bg-dark text-white p-8">
      <h1 className="text-2xl font-bold text-neon-cyan mb-4">Strategies</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {strategies.map((strategy) => (
          <div key={strategy.name} className="bg-glass rounded-xl p-6 shadow-neon-magenta backdrop-blur-xs">
            <h2 className="text-xl font-semibold text-neon-magenta">{strategy.name}</h2>
            <p>Type: {strategy.type}</p>
            {/* Add more strategy details here */}
          </div>
        ))}
      </div>
      <div className="mt-8 bg-glass rounded-xl p-6 shadow-neon-lime backdrop-blur-xs">
        <h2 className="text-xl font-semibold mb-4 text-neon-lime">Strategy Marketplace</h2>
        {/* Placeholder for strategy marketplace integration */}
        <p>Discover and import new trading strategies from the community marketplace.</p>
        <button className="mt-4 bg-neon-lime text-bg-dark font-bold py-2 px-4 rounded shadow-neon-lime hover:bg-neon-cyan transition">Browse Marketplace</button>
      </div>
    </div>
  );
}