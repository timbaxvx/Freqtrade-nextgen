import React from "react";

export default function BotStatusGrid() {
  // Platzhalter für Bot-Status
  return (
    <div className="grid grid-cols-2 gap-4">
      <div className="bg-bg-dark p-4 rounded shadow-neon-cyan">
        <h3 className="text-neon-cyan">Bot Alpha</h3>
        <p>Status: <span className="text-neon-lime">Running</span></p>
      </div>
      <div className="bg-bg-dark p-4 rounded shadow-neon-magenta">
        <h3 className="text-neon-magenta">Bot Beta</h3>
        <p>Status: <span className="text-neon-magenta">Stopped</span></p>
      </div>
    </div>
  );
}