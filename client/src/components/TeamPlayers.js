import { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import Table from 'react-bootstrap/Table';

function TeamPlayers() {
  const { team_id } = useParams();
  const [players, setPlayers] = useState([]);

  useEffect(() => {
    fetch('/teams/' + team_id)
      .then(response => response.json())
      .then(data => setPlayers(data.players))
      .catch(error => console.log(error));
  }, [team_id]);
  return (
    <div>
      <h1>Team Players</h1>
      <Table striped bordered hover size="sm">
        <thead>
          <tr>
            <th>Position</th>
            <th>Name</th>
            <th>Contact</th>
            <th>Power</th>
            <th>Velocity</th>
          </tr>
        </thead>
        <tbody>
          {players.map(player => 
            <tr key={player.id}>
              <td>{player.position}</td>
              <td><Link to={"/player/" + player.id}>{player.first_name} {player.last_name}</Link></td>
              <td>{player.contact}</td>
              <td>{player.power}</td>
              <td>{player.velocity}</td>
            </tr>
          )}
        </tbody>
      </Table>
    </div>
  );
}

export default TeamPlayers;
