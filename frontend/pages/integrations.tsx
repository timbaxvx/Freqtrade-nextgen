import React, { useEffect, useState } from "react";

interface Account {
  id: number;
  name: string;
  exchange: string;
}

export default function Integrations() {
  const [accounts, setAccounts] = useState<Account[]>([]);

  useEffect(() => {
    const fetchAccounts = async () => {
      try {
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/integrations/accounts`, {
          headers: {
            'Authorization': 'Bearer YOUR_AUTH_TOKEN' // Replace with actual token
          }
        });
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data: Account[] = await response.json();
        setAccounts(data);
      } catch (error) {
        console.error("Error fetching accounts:", error);
      }
    };
    fetchAccounts();
  }, []);

  return (
    <div className="min-h-screen bg-bg-dark text-white p-8">
      <h1 className="text-2xl font-bold text-neon-cyan mb-4">Integrations</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {accounts.map((account) => (
          <div key={account.id} className="bg-glass rounded-xl p-6 shadow-neon-magenta backdrop-blur-xs">
            <h2 className="text-xl font-semibold text-neon-magenta">{account.name}</h2>
            <p>Exchange: {account.exchange}</p>
            {/* Add more account details here */}
          </div>
        ))}
      </div>
      <div className="mt-8 bg-glass rounded-xl p-6 shadow-neon-lime backdrop-blur-xs">
        <h2 className="text-xl font-semibold mb-4 text-neon-lime">Plugin Marketplace</h2>
        {/* Placeholder for plugin marketplace integration */}
        <p>Discover and install new plugins to enhance your integrations.</p>
        <button className="mt-4 bg-neon-lime text-bg-dark font-bold py-2 px-4 rounded shadow-neon-lime hover:bg-neon-cyan transition">Browse Plugin Marketplace</button>
      </div>
    </div>
  );
}