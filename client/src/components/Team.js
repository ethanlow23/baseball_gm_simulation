import { useState, useEffect } from 'react';

function Team() {
  const [team, setTeam] = useState({});
  const [players, setPlayers] = useState([]);
  useEffect(() => {
    fetch('teams')
      .then(response => response.json())
      .then(data => {
        console.log(data);
        setTeam(data[0]);
        setPlayers(data[0].players);
      })
      .catch(error => console.log(error));
  }, []);
  return (
    <div>
      <h1>Team Information Page</h1>
      <h3>{team.city} {team.name}</h3>
      <ul>
        {players.map(player =>
          <li>{player.first_name} {player.last_name}</li>
        )}
      </ul>
    </div>
  );
}

export default Team;
