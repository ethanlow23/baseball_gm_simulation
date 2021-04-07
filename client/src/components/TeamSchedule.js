import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Table from 'react-bootstrap/Table';

function TeamSchedule() {
  const { team_id } = useParams();
  const [games, setGames] = useState([]);

  useEffect(() => {
    fetch('/teams/' + team_id + '/schedule')
      .then(response => response.json())
      .then(data => setGames(data))
      .catch(error => console.log(error));
  }, [team_id]);

  return (
    <div>
      <h1>Team Schedule</h1>
      <Table striped bordered hover size="sm">
        <thead>
          <tr>
            <th>Game No.</th>
            <th>Away</th>
            <th>Home</th>
          </tr>
        </thead>
        <tbody>
          {games.map(game => 
            <tr key={game.id}>
              <td>{game.game_number}</td>
              <td>{game.away_team}</td>
              <td>{game.home_team}</td>
            </tr>
          )}
        </tbody>
      </Table>
    </div>
  );
}

export default TeamSchedule;
