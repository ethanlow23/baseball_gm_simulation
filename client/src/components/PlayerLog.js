import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function PlayerLog() {
  const [log, setLog] = useState([]);

  useEffect(() => {
    fetch('/players/1/log')
      .then(response => response.json())
      .then(data => {
        setLog(data.games);
      })
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>Player Log</h1>
      <table>
        <thead>
          <tr>
            <th>Game</th>
            <th>AB</th>
            <th>H</th>
            <th>HR</th>
            <th>2B</th>
            <th>3B</th>
            <th>RBI</th>
            <th>AVG</th>
          </tr>
        </thead>
        <tbody>
          {log.map(game => 
            <tr>
              <td><Link to="/games">{game.game_teams[0].city} {game.game_teams[0].name} vs {game.game_teams[1].city} {game.game_teams[1].name}</Link></td>
              <td>{game.stats.at_bats}</td>
              <td>{game.stats.hits}</td>
              <td>{game.stats.homeruns}</td>
              <td>{game.stats.doubles}</td>
              <td>{game.stats.doubles}</td>
              <td>{game.stats.rbi}</td>
              <td>{(game.stats.hits / game.stats.at_bats).toFixed(3)}</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default PlayerLog;
