import { useState, useEffect } from 'react';
import Table from 'react-bootstrap/Table';

function LeagueStats () {
  const [teamsStats, setTeamsStats] = useState([]);

  useEffect(() => {
    fetch('/league/stats')
      .then(response => response.json())
      .then(data => setTeamsStats(data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>League Stats</h1>
      <Table striped bordered hover size="sm">
        <thead>
          <tr>
            <th>Team</th>
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
          {teamsStats.map(stat => 
            <tr key={stat.team.id}>
              <td>{stat.team.city} {stat.team.name}</td>
              <td>{stat.AB}</td>
              <td>{stat.H}</td>
              <td>{stat.HR}</td>
              <td>{stat['2B']}</td>
              <td>{stat['3B']}</td>
              <td>{stat.RBI}</td>
              <td>{(stat.H / stat.AB).toFixed(3)}</td>
            </tr>
          )}
        </tbody>
      </Table>
    </div>
  );
}

export default LeagueStats;
