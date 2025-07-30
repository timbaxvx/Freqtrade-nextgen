import React from "react";

export default function Settings() {
  return (
    <div className="min-h-screen bg-bg-dark text-white p-8">
      <h1 className="text-2xl font-bold text-neon-cyan mb-4">Settings</h1>
      <div classNameName="bg-glass rounded-xl p-6 shadow-neon-cyan backdrop-blur-xs">
        <h2 className="text-xl font-semibold mb-4 text-neon-cyan">User Profile</h2>
        {/* Placeholder for user profile settings */}
        <p>Email: user@example.com</p>
        <button className="mt-4 bg-neon-cyan text-bg-dark font-bold py-2 px-4 rounded shadow-neon-cyan hover:bg-neon-lime transition">Update Profile</button>
      </div>
      <div className="mt-8 bg-glass rounded-xl p-6 shadow-neon-magenta backdrop-blur-xs">
        <h2 className="text-xl font-semibold mb-4 text-neon-magenta">Notifications</h2>
        {/* Placeholder for notification settings */}
        <label className="inline-flex items-center">
          <input type="checkbox" className="form-checkbox" checked />
          <span className="ml-2">Enable Email Notifications</span>
        </label>
      </div>
      <div className="mt-8 bg-glass rounded-xl p-6 shadow-neon-lime backdrop-blur-xs">
        <h2 className="text-xl font-semibold mb-4 text-neon-lime">Plugin Management</h2>
        {/* Placeholder for plugin system integration */}
        <p>Discover and manage plugins to extend Freqtrade NextGen functionality.</p>
        <button className="mt-4 bg-neon-lime text-bg-dark font-bold py-2 px-4 rounded shadow-neon-lime hover:bg-neon-cyan transition">Browse Plugins</button>
      </div>
    </div>
  );
}