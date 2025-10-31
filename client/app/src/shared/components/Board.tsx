import React, { useEffect, useState } from 'react';

interface Team {
  teamName: string;
  score: number;
}

interface Game {
  homeTeam: Team;
  awayTeam: Team;
}

function LiveScores(): JSX.Element {
  const [games, setGames] = useState<Game[]>([]);
  const [connectionStatus, setConnectionStatus] = useState<string>("Connecting...");

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/sb/live-scores');

    ws.onopen = () => setConnectionStatus('Connected');
    ws.onmessage = (event: MessageEvent) => {
      const data: Game[] = JSON.parse(event.data);
      setGames(data);
    };
    ws.onclose = () => setConnectionStatus('Disconnected');
    ws.onerror = () => setConnectionStatus('Error');

    return () => ws.close();
  }, []);

  return (
    <div>
      <h1 className="text-xl">Scoreboard</h1>
      <p>Status: {connectionStatus}</p>
      {games.map((game, index) => (
        <div key={index}>
          {game.homeTeam.teamName} vs {game.awayTeam.teamName}:
          {game.homeTeam.score} - {game.awayTeam.score}
        </div>
      ))}
    </div>
  );
}

export default LiveScores;
