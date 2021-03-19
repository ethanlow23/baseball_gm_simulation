import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

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
          <li key={player.id}><Link to={"/player/" + player.id}>{player.first_name} {player.last_name}</Link></li>
        )}
      </ul>
    </div>
  );
}

export default TeamPlayers;
