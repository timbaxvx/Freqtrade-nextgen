import React, { useEffect, useState } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

export default function Analytics() {
  const [portfolioData, setPortfolioData] = useState<any>(null);
  const [chartData, setChartData] = useState<any[]>([]);

  useEffect(() => {
    const fetchPortfolioData = async () => {
      try {
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/analytics/portfolio`, {
          headers: {
            'Authorization': 'Bearer YOUR_AUTH_TOKEN' // Replace with actual token
          }
        });
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setPortfolioData(data);

        // Dummy data for chart
        setChartData([
          { name: 'Jan', value: 4000 },
          { name: 'Feb', value: 3000 },
          { name: 'Mar', value: 2000 },
          { name: 'Apr', value: 2780 },
          { name: 'May', value: 1890 },
          { name: 'Jun', value: 2390 },
          { name: 'Jul', value: 3490 },
        ]);

      } catch (error) {
        console.error("Error fetching portfolio data:", error);
      }
    };
    fetchPortfolioData();
  }, []);

  return (
    <div className="min-h-screen bg-bg-dark text-white p-8">
      <h1 className="text-2xl font-bold text-neon-cyan mb-4">Analytics</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <section className="bg-glass rounded-xl p-6 shadow-neon-cyan backdrop-blur-xs">
          <h2 className="text-xl font-semibold mb-4 text-neon-cyan">Portfolio Performance</h2>
          {portfolioData ? (
            <div>
              <p>PNL: {portfolioData.pnl}</p>
              <p>Sharpe Ratio: {portfolioData.sharpe}</p>
              <p>Drawdown: {portfolioData.drawdown}</p>
              <p>Total Value: {portfolioData.total_value}</p>
            </div>
          ) : (
            <p>Loading portfolio data...</p>
          )}
        </section>
        <section className="bg-glass rounded-xl p-6 shadow-neon-magenta backdrop-blur-xs">
          <h2 className="text-xl font-semibold mb-4 text-neon-magenta">Portfolio Chart</h2>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={chartData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#333" />
              <XAxis dataKey="name" stroke="#00FFF7" />
              <YAxis stroke="#00FFF7" />
              <Tooltip contentStyle={{ backgroundColor: '#181A20', border: '1px solid #00FFF7' }} />
              <Legend />
              <Line type="monotone" dataKey="value" stroke="#B6FF00" activeDot={{ r: 8 }} />
            </LineChart>
          </ResponsiveContainer>
        </section>
      </div>
    </div>
  );
}