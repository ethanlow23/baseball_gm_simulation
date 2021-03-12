import { useState, useEffect } from 'react';

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
      <ul>
        {stats.map(stat => 
          <li>{stat.player.first_name} {stat.player.last_name} - AB: {stat.AB} H: {stat.H} HR: {stat.HR} 2B: {stat['2B']} 3B: {stat['3B']} RBI: {stat.RBI} AVG: {(stat.H / stat.AB).toFixed(3)}</li>
        )}
      </ul>
    </div>
  );
}

export default TeamStats;
