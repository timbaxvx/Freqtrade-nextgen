import React, { useCallback } from "react";
import ReactFlow, { 
  MiniMap, 
  Controls, 
  Background, 
  useNodesState, 
  useEdgesState, 
  addEdge, 
  Connection,
  Edge
} from 'reactflow';

import 'reactflow/dist/style.css';

const initialNodes = [
  { id: '1', position: { x: 0, y: 0 }, data: { label: 'RSI Indicator' } },
  { id: '2', position: { x: 0, y: 100 }, data: { label: 'EMA Indicator' } },
];
const initialEdges = [];

export default function StrategyBuilder() {
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);

  const onConnect = useCallback((params: Connection | Edge) => setEdges((eds) => addEdge(params, eds)), []);

  return (
    <div className="min-h-screen bg-bg-dark text-white p-8">
      <h1 className="text-2xl font-bold text-neon-cyan mb-4">Strategie-Builder</h1>
      <div className="flex gap-8 h-[calc(100vh-150px)]">
        <aside className="w-1/4 bg-glass p-4 rounded shadow-neon-magenta">
          <h2 className="text-neon-magenta mb-2">Toolbox</h2>
          <ul>
            <li className="p-2 bg-bg-dark rounded mb-2 cursor-grab">Indikator: RSI</li>
            <li className="p-2 bg-bg-dark rounded mb-2 cursor-grab">Indikator: EMA</li>
            <li className="p-2 bg-bg-dark rounded mb-2 cursor-grab">Operator: AND</li>
            <li className="p-2 bg-bg-dark rounded mb-2 cursor-grab">KI-Block</li>
          </ul>
        </aside>
        <main className="flex-1 bg-glass p-4 rounded shadow-neon-cyan relative">
          <h2 className="text-neon-cyan mb-2">Flowchart-Canvas</h2>
          <ReactFlow
            nodes={nodes}
            edges={edges}
            onNodesChange={onNodesChange}
            onEdgesChange={onEdgesChange}
            onConnect={onConnect}
            fitView
          >
            <MiniMap />
            <Controls />
            <Background variant="dots" gap={12} size={1} />
          </ReactFlow>
        </main>
        <aside className="w-1/4 bg-glass p-4 rounded shadow-neon-lime">
          <h2 className="text-neon-lime mb-2">Backtest</h2>
          <div className="bg-bg-dark p-2 rounded">
            <p>Resultate: [PnL, Sharpe, Drawdown]</p>
          </div>
        </aside>
      </div>
    </div>
  );
}