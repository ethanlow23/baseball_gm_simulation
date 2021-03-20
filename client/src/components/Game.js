import { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';

function Game() {
  const { game_id } = useParams();
  const [gameInfo, setGameInfo] = useState({});
  const [t1TeamStats, setT1TeamStats] = useState({});
  const [t2TeamStats, setT2TeamStats] = useState({});
  const [t1PlayerStats, setT1PlayerStats] = useState([]);
  const [t2PlayerStats, setT2PlayerStats] = useState([]);

  useEffect(() => {
    fetch('/games/' + game_id)
      .then(response => response.json())
      .then(data => {
        setGameInfo(data);
        setT1TeamStats(data.t1_team_stats);
        setT2TeamStats(data.t2_team_stats);
        setT1PlayerStats(data.t1_player_stats);
        setT2PlayerStats(data.t2_player_stats);
      })
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>Game Information</h1>
      <h3>{gameInfo.t1} {gameInfo.t1_score} - {gameInfo.t2_score} {gameInfo.t2}</h3>
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
          {t1PlayerStats.map(stat =>
            <tr>
              <td><Link to={"/player/" + stat.player_id}>{stat.player_id}</Link></td>
              <td>{stat.at_bats}</td>
              <td>{stat.hits}</td>
              <td>{stat.homeruns}</td>
              <td>{stat.doubles}</td>
              <td>{stat.triples}</td>
              <td>{stat.rbi}</td>
              <td>{(stat.hits / stat.at_bats).toFixed(3)}</td>
            </tr>
          )}
        </tbody>
      </table>
      <table>
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
          <tr>
            <td>{gameInfo.t1}</td>
            <td>{t1TeamStats.at_bats}</td>
            <td>{t1TeamStats.hits}</td>
            <td>{t1TeamStats.homeruns}</td>
            <td>{t1TeamStats.doubles}</td>
            <td>{t1TeamStats.triples}</td>
            <td>{t1TeamStats.rbi}</td>
            <td>{(t1TeamStats.hits / t1TeamStats.at_bats).toFixed(3)}</td>
          </tr>
        </tbody>
      </table>
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
          {t2PlayerStats.map(stat =>
            <tr>
              <td><Link to={"/player/" + stat.player_id}>{stat.player_id}</Link></td>
              <td>{stat.at_bats}</td>
              <td>{stat.hits}</td>
              <td>{stat.homeruns}</td>
              <td>{stat.doubles}</td>
              <td>{stat.triples}</td>
              <td>{stat.rbi}</td>
              <td>{(stat.hits / stat.at_bats).toFixed(3)}</td>
            </tr>
          )}
        </tbody>
      </table>
      <table>
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
          <tr>
            <td>{gameInfo.t2}</td>
            <td>{t2TeamStats.at_bats}</td>
            <td>{t2TeamStats.hits}</td>
            <td>{t2TeamStats.homeruns}</td>
            <td>{t2TeamStats.doubles}</td>
            <td>{t2TeamStats.triples}</td>
            <td>{t2TeamStats.rbi}</td>
            <td>{(t2TeamStats.hits / t2TeamStats.at_bats).toFixed(3)}</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default Game;
