import { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import Table from 'react-bootstrap/Table';

function TeamStats() {
  const { team_id } = useParams();
  const [battersStats, setBattersStats] = useState([]);
  const [pitchersStats, setPitchersStats] = useState([]);

  useEffect(() => {
    fetch('/teams/' + team_id + '/stats')
      .then(response => response.json())
      .then(data => {
        setBattersStats(data.batters);
        setPitchersStats(data.pitchers);
      })
      .catch(error => console.log(error));
  }, [team_id]);

  return (
    <div>
      <h1>Team Stats</h1>
      <h3>Batting</h3>
      <Table striped bordered hover size="sm">
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
          {battersStats.map(batter => 
            <tr key={batter.player.id}>
              <td><Link to={"/player/" + batter.player.id}>{batter.player.first_name} {batter.player.last_name}</Link></td>
              <td>{batter.AB}</td>
              <td>{batter.H}</td>
              <td>{batter.HR}</td>
              <td>{batter['2B']}</td>
              <td>{batter['3B']}</td>
              <td>{batter.RBI}</td>
              <td>{(batter.H / batter.AB).toFixed(3)}</td>
            </tr>
          )}
        </tbody>
      </Table>
      <h3>Pitching</h3>
      <Table striped bordered hover size="sm">
        <thead>
          <tr>
            <th>Player</th>
          </tr>
        </thead>
        <tbody>
          {pitchersStats.map(pitcher =>
            <tr key={pitcher.player.id}>
              <td><Link to={"/player/" + pitcher.player.id}>{pitcher.player.first_name} {pitcher.player.last_name}</Link></td>
            </tr>
          )}
        </tbody>
      </Table>
    </div>
  );
}

export default TeamStats;
