import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Table from 'react-bootstrap/Table';

function PlayerStats() {
  const { player_id } = useParams();
  const [stats, setStats] = useState({});

  useEffect(() => {
    fetch('/players/' + player_id + '/stats')
      .then(response => response.json())
      .then(data => setStats(data))
      .catch(error => console.log(error));
  }, [player_id]);

  return (
    <div>
      <h1>Player Career Stats</h1>
      <Table>
        <thead>
          <tr>
            <th>Season</th>
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
          {Object.keys(stats).map((year, i) =>
            <tr key={i}>
              <td>{year}</td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
              <td></td>
            </tr>
          )}
        </tbody>
      </Table>
    </div>
  );
}

export default PlayerStats;
