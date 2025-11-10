import React, { useEffect, useState } from 'react';

interface Team {
  teamName: string;
}

interface Game {
  homeTeam: Team;
  awayTeam: Team;
}

interface AwayLeader {
  teamTricode: string;
  name: string;
  points: number;
  rebounds: number;
  assists: number;
}

function LiveLeaders(): JSX.Element {
  const [awayLeader, setAwayLeader] = useState<AwayLeader[]>([]);
  const [games, setGames] = useState<Game[]>([]);
  const [connectionStatus, setConnectionStatus] = useState<string>("Loading...");

  useEffect(() => {
    const ws = new WebSocket(`ws://localhost:8000/sb/live-leaders`);

    ws.onopen = () => setConnectionStatus('Connected');
    ws.onmessage = (event: MessageEvent) => {
      const data: Game[] = JSON.parse(event.data);
      const leaderData: AwayLeader[] = JSON.parse(event.data);
      setGames(data);
      setAwayLeader(leaderData);
    };
    ws.onclose = () => setConnectionStatus('Disconnected');
    ws.onerror = () => setConnectionStatus('Error');


    return () => ws.close();
  }, []);

  return (
    <div>
      <h2 className='text-md'>Away Team</h2>
      {games.map((game, index) => (
        <div key={index}>
          <h3>{game.awayTeam.teamName}<br /></h3>
        </div>
      ))}
      {awayLeader.map((player, index) => (
        <div key={index}>
          <h3>{player.name}</h3>
        </div>
      ))}
    </div>

  )
}

export default LiveLeaders;
