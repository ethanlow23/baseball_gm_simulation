import { useState, useEffect } from 'react';

function TeamSchedule() {
  const [games, setGames] = useState([]);

  useEffect(() => {
    fetch('/teams/1/schedule')
      .then(response => response.json())
      .then(data => setGames(data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>Team Schedule</h1>
      <ul>
        {games.map(game => 
          <li>{game.team1.city} {game.team1.name} {game.team1_score} vs {game.team2.city} {game.team2.name} {game.team2_score}</li>
        )}
      </ul>
    </div>
  );
}

export default TeamSchedule;
