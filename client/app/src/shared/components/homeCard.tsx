import React, { useEffect, useState } from 'react';

interface Player {
  teamName: string;
  playerName: string;
  score: number;
}

interface Game {
  homeTeam: string;
  awayTeam: string;
}

function LiveLeaders(): JSX.Element {
  const [player, setPlayer] = useState<Player[]>([]);
  const [games, setGames] = useState<Game[]>([]);
  const [connectionStatus, setConnectionStatus] = useState<string>("Loading...");

  useEffect(() => {
    const ws = new WebSocket(`ws://localhost:8000/`);

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
      <h2 className='text-md'>Home Team</h2>
    </div>
  )
}
