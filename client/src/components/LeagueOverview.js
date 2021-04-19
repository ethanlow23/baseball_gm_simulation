import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import ListGroup from 'react-bootstrap/ListGroup';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Table from 'react-bootstrap/Table';

function LeagueOverview() {
  const [recentResults, setRecentResults] = useState([]);
  const [upcomingGames, setUpcomingGames] = useState([]);
  const [topTeams, setTopTeams] = useState([]);
  const [topPlayers, setTopPlayers] = useState([]);

  useEffect(() => {
    fetch('/league/overview')
      .then(response => response.json())
      .then(data => {
        setRecentResults(data.recent_results);
        setUpcomingGames(data.upcoming_games);
        setTopTeams(data.top_teams);
        setTopPlayers(data.top_players);
      })
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>League Overview</h1>
      <Row>
        <Col>
          <h3>Recent Games</h3>
          <ListGroup>
            {recentResults.map(result =>
              <ListGroup.Item><Link to={"/game/" + result.id}>{result.away} {result.away_score}-{result.home_score} {result.home}</Link></ListGroup.Item>
            )}
          </ListGroup>
        </Col>
        <Col>
          <h3>Top Teams</h3>
          <Table>
            <thead>
              <tr>
                <th>Team</th>
                <th>Wins</th>
                <th>Losses</th>
              </tr>
            </thead>
            <tbody>
              {topTeams.map(team =>
                <tr>
                  <td><Link to={"/team/" + team.id}>{team.city} {team.name}</Link></td>
                  <td>0</td>
                  <td>0</td>
                </tr>
              )}
            </tbody>
          </Table>
        </Col>
      </Row>
      <Row>
        <Col>
          <h3>Upcoming Games</h3>
          <ListGroup>
            {upcomingGames.map(game =>
              <ListGroup.Item>{game.away} vs {game.home}</ListGroup.Item>
            )}
          </ListGroup>
        </Col>
        <Col>
          <h3>Top Players</h3>
          <Table>
            <thead>
              <tr>
                <th>Player</th>
                <th>Wins</th>
                <th>Losses</th>
              </tr>
            </thead>
            <tbody>
              {topPlayers.map(player =>
                <tr>
                  <td><Link to={"/player/" + player.id}>{player.first_name} {player.last_name}</Link></td>
                  <td>0</td>
                  <td>0</td>
                </tr>
              )}
            </tbody>
          </Table>
        </Col>
      </Row>
    </div>
  );
}

export default LeagueOverview;
