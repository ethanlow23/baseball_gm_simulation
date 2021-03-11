import { useState, useEffect } from 'react';

function TeamPlayers() {
  const [players, setPlayers] = useState([]);

  useEffect(() => {
    fetch('/teams/1')
      .then(response => response.json())
      .then(data => setPlayers(data.players))
      .catch(error => console.log(error));
  }, []);
  return (
    <div>
      <h1>Team Players</h1>
      <ul>
        {players.map(player =>
          <li key={player.id}>{player.first_name} {player.last_name}</li>
        )}
      </ul>
    </div>
  );
}

export default TeamPlayers;
