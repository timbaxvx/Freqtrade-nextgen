import React from "react";
import GPTAssistant from "../components/GPTAssistant";

export default function Assistant() {
  return (
    <div className="min-h-screen bg-bg-dark text-white p-8">
      <h1 className="text-2xl font-bold text-neon-cyan mb-4">AI Assistant</h1>
      <div className="bg-glass rounded-xl p-6 shadow-neon-cyan backdrop-blur-xs">
        <GPTAssistant />
      </div>
    </div>
  );
}