import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function TeamStats() {
  const [stats, setStats] = useState([]);

  useEffect(() => {
    fetch('/teams/1/stats')
      .then(response => response.json())
      .then(data => setStats(data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>Team Stats</h1>
      <table>
        <thead>
          <tr>
            <th>Player</th>
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
          {stats.map(stat => 
            <tr>
              <td><Link to="/player">{stat.player.first_name} {stat.player.last_name}</Link></td>
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
      </table>
    </div>
  );
}

export default TeamStats;
