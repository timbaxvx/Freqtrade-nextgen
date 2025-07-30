import React, { useEffect, useState } from "react";
import { Bot } from "../../shared/types";

export default function Bots() {
  const [bots, setBots] = useState<Bot[]>([]);

  useEffect(() => {
    // Fetch bots from backend
    const fetchBots = async () => {
      try {
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/bots`, {
          headers: {
            'Authorization': 'Bearer YOUR_AUTH_TOKEN' // Replace with actual token
          }
        });
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data: Bot[] = await response.json();
        setBots(data);
      } catch (error) {
        console.error("Error fetching bots:", error);
      }
    };
    fetchBots();
  }, []);

  return (
    <div className="min-h-screen bg-bg-dark text-white p-8">
      <h1 className="text-2xl font-bold text-neon-cyan mb-4">Bots</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {bots.map((bot) => (
          <div key={bot.name} className="bg-glass rounded-xl p-6 shadow-neon-cyan backdrop-blur-xs">
            <h2 className="text-xl font-semibold text-neon-cyan">{bot.name}</h2>
            <p>Status: <span className={bot.status === "running" ? "text-neon-lime" : "text-neon-magenta"}>{bot.status}</span></p>
            {/* Add more bot details here */}
          </div>
        ))}
      </div>
    </div>
  );
}