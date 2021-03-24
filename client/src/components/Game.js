import { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';

function Game() {
  const { game_id } = useParams();
  const [gameInfo, setGameInfo] = useState({});
  const [awayTeamStats, setAwayTeamStats] = useState({});
  const [homeTeamStats, setHomeTeamStats] = useState({});
  const [awayPlayerStats, setAwayPlayerStats] = useState([]);
  const [homePlayerStats, setHomePlayerStats] = useState([]);

  useEffect(() => {
    fetch('/games/' + game_id)
      .then(response => response.json())
      .then(data => {
        setGameInfo(data);
        setAwayTeamStats(data.away_team_stats);
        setHomeTeamStats(data.home_team_stats);
        setAwayPlayerStats(data.away_player_stats);
        setHomePlayerStats(data.home_player_stats);
      })
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>Game Information</h1>
      <h3>{gameInfo.away} {gameInfo.away_score} - {gameInfo.home_score} {gameInfo.home}</h3>
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
          {awayPlayerStats.map(player =>
            <tr>
              <td><Link to={"/player/" + player.id}>{player.name}</Link></td>
              <td>{player.stats.at_bats}</td>
              <td>{player.stats.hits}</td>
              <td>{player.stats.homeruns}</td>
              <td>{player.stats.doubles}</td>
              <td>{player.stats.triples}</td>
              <td>{player.stats.rbi}</td>
              <td>{(player.stats.hits / player.stats.at_bats).toFixed(3)}</td>
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
            <td>{gameInfo.away}</td>
            <td>{awayTeamStats.at_bats}</td>
            <td>{awayTeamStats.hits}</td>
            <td>{awayTeamStats.homeruns}</td>
            <td>{awayTeamStats.doubles}</td>
            <td>{awayTeamStats.triples}</td>
            <td>{awayTeamStats.rbi}</td>
            <td>{(awayTeamStats.hits / awayTeamStats.at_bats).toFixed(3)}</td>
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
          {homePlayerStats.map(player =>
            <tr>
              <td><Link to={"/player/" + player.id}>{player.name}</Link></td>
              <td>{player.stats.at_bats}</td>
              <td>{player.stats.hits}</td>
              <td>{player.stats.homeruns}</td>
              <td>{player.stats.doubles}</td>
              <td>{player.stats.triples}</td>
              <td>{player.stats.rbi}</td>
              <td>{(player.stats.hits / player.stats.at_bats).toFixed(3)}</td>
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
            <td>{gameInfo.home}</td>
            <td>{homeTeamStats.at_bats}</td>
            <td>{homeTeamStats.hits}</td>
            <td>{homeTeamStats.homeruns}</td>
            <td>{homeTeamStats.doubles}</td>
            <td>{homeTeamStats.triples}</td>
            <td>{homeTeamStats.rbi}</td>
            <td>{(homeTeamStats.hits / homeTeamStats.at_bats).toFixed(3)}</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default Game;
