import React, { useState } from "react";

export default function GPTAssistant() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Wie kann ich beim Trading helfen?" }
  ]);

  const sendMessage = async () => {
    setMessages([...messages, { role: "user", content: input }]);
    setInput("");
    // Here you would make the actual API call to your backend's /ai/generate_text endpoint
    // For now, we'll use a dummy response.
    setTimeout(() => {
      setMessages(msgs => [...msgs, { role: "assistant", content: "Das ist eine KI-generierte Antwort." }]);
    }, 1000);
  };

  const startVoiceInput = () => {
    alert("Voice input not yet implemented.");
    // In a real application, you would use the Web Speech API (SpeechRecognition)
  };

  return (
    <div className="flex flex-col gap-2">
      <div className="h-32 overflow-y-auto bg-bg-dark p-2 rounded">
        {messages.map((msg, i) => (
          <div key={i} className={msg.role === "assistant" ? "text-neon-cyan" : "text-neon-magenta"}>
            <b>{msg.role === "assistant" ? "GPT" : "Du"}:</b> {msg.content}
          </div>
        ))}
      </div>
      <div className="flex gap-2">
        <input
          className="flex-1 p-2 rounded bg-glass text-white"
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Frage stellen..."
        />
        <button onClick={sendMessage} className="bg-neon-cyan text-bg-dark px-4 py-2 rounded shadow-neon-cyan">Senden</button>
        <button onClick={startVoiceInput} className="bg-neon-magenta text-bg-dark px-4 py-2 rounded shadow-neon-magenta">Voice</button>
      </div>
    </div>
  );
}