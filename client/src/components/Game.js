import { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Table from 'react-bootstrap/Table';

function Game() {
  const { game_id } = useParams();
  const [gameInfo, setGameInfo] = useState({});
  const [awayTeam, setAwayTeam] = useState({});
  const [homeTeam, setHomeTeam] = useState({});
  const [awayTeamStats, setAwayTeamStats] = useState({});
  const [homeTeamStats, setHomeTeamStats] = useState({});
  const [awayPlayerStats, setAwayPlayerStats] = useState([]);
  const [homePlayerStats, setHomePlayerStats] = useState([]);

  useEffect(() => {
    fetch('/games/' + game_id)
      .then(response => response.json())
      .then(data => {
        setGameInfo(data);
        setAwayTeam(data.away);
        setHomeTeam(data.home);
        setAwayTeamStats(data.away_team_stat);
        setHomeTeamStats(data.home_team_stat);
        setAwayPlayerStats(data.away_player_stats);
        setHomePlayerStats(data.home_player_stats);
      })
      .catch(error => console.log(error));
  }, [game_id]);

  return (
    <div>
      <Jumbotron>
        <h1>Game Information</h1>
        <h3>{awayTeam.city} {awayTeam.name} {gameInfo.away_score} - {gameInfo.home_score} {homeTeam.city} {homeTeam.name}</h3>
      </Jumbotron>
      <h1>Batting</h1>
      <Row>
        <Col>
          <Table striped bordered size="sm">
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
              {awayPlayerStats.map(stat =>
                <tr>
                  <td><Link to={"/player/" + stat.player.id}>{stat.player.first_name} {stat.player.last_name}</Link></td>
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
          </Table>
          <Table striped bordered size="sm">
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
                <td>{awayTeam.city} {awayTeam.name}</td>
                <td>{awayTeamStats.at_bats}</td>
                <td>{awayTeamStats.hits}</td>
                <td>{awayTeamStats.homeruns}</td>
                <td>{awayTeamStats.doubles}</td>
                <td>{awayTeamStats.triples}</td>
                <td>{awayTeamStats.rbi}</td>
                <td>{(awayTeamStats.hits / awayTeamStats.at_bats).toFixed(3)}</td>
              </tr>
            </tbody>
          </Table>
        </Col>
        <Col>
          <Table striped bordered size="sm">
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
              {homePlayerStats.map(stat =>
                <tr>
                  <td><Link to={"/player/" + stat.player.id}>{stat.player.first_name} {stat.player.last_name}</Link></td>
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
          </Table>
          <Table striped bordered size="sm">
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
                <td>{homeTeam.city} {homeTeam.name}</td>
                <td>{homeTeamStats.at_bats}</td>
                <td>{homeTeamStats.hits}</td>
                <td>{homeTeamStats.homeruns}</td>
                <td>{homeTeamStats.doubles}</td>
                <td>{homeTeamStats.triples}</td>
                <td>{homeTeamStats.rbi}</td>
                <td>{(homeTeamStats.hits / homeTeamStats.at_bats).toFixed(3)}</td>
              </tr>
            </tbody>
          </Table>
        </Col>
      </Row>
      <h1>Pitching</h1>
    </div>
  );
}

export default Game;
