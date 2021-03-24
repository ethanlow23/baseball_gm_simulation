import { useState, useEffect } from 'react';

function LeagueTeams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('/league/teams')
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.log(error));
  });

  return (
    <div>
      <h1>League Teams</h1>
      <ul>
        {teams.map(team => 
          <li key={team.id}>{team.city} {team.name}</li>
        )}
      </ul>
    </div>
  );
}

export default LeagueTeams;
