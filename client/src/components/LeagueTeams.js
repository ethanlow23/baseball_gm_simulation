import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import ListGroup from 'react-bootstrap/ListGroup';

function LeagueTeams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('/league/teams')
      .then(response => response.json())
      .then(data => setTeams(data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>League Teams</h1>
      <ListGroup>
        {teams.map(team => 
          <ListGroup.Item as={Link} to={"/team/" + team.id} key={team.id}>{team.city} {team.name}</ListGroup.Item>
        )}
      </ListGroup>
    </div>
  );
}

export default LeagueTeams;
