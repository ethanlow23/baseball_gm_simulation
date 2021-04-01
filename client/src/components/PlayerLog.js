import { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import Table from 'react-bootstrap/Table';

function PlayerLog() {
  const { player_id } = useParams();
  const [log, setLog] = useState([]);

  useEffect(() => {
    fetch('/players/' + player_id + '/log')
      .then(response => response.json())
      .then(data => setLog(data.games))
      .catch(error => console.log(error));
  }, [player_id]);

  return (
    <div>
      <h1>Player Log</h1>
      <Table striped bordered hover size="sm">
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
            <tr key={game.game_id}>
              <td><Link to={"/game/" + game.game_id}>{game.away_team.city} {game.away_team.name} vs {game.home_team.city} {game.home_team.name}</Link></td>
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
      </Table>
    </div>
  );
}

export default PlayerLog;
