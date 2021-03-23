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
          <li key={game.id}>{game.game_number}. {game.away_team} vs {game.home_team}</li>
        )}
      </ul>
    </div>
  );
}

export default TeamSchedule;
