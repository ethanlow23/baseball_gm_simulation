import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import ListGroup from 'react-bootstrap/ListGroup';

function TeamOverview() {
  const { team_id } = useParams();
  const [wins, setWins] = useState(0);
  const [losses, setLosses] = useState(0);
  const [recentResults, setRecentResults] = useState([]);
  const [upcomingGames, setUpcomingGames] = useState([]);
  const [topPlayers, setTopPlayers] = useState([]);

  useEffect(() => {
    fetch('/teams/' + team_id + '/overview')
      .then(response => response.json())
      .then(data => {
        setWins(data.wins);
        setLosses(data.losses);
        setRecentResults(data.recent_results);
        setUpcomingGames(data.upcoming_games);
        setTopPlayers(data.top_performers);
      })
      .catch(error => console.log(error));
  }, [team_id]);

  return(
    <div>
      <h1>Team Overview</h1>
      <h3>{wins} - {losses}</h3>
      <Row>
        <Col>
          <h3>Recent Games</h3>
          <ListGroup>
            {recentResults.map(result =>
              <ListGroup.Item>{result.game_number}</ListGroup.Item>
            )}
          </ListGroup>
        </Col>
        <Col>
          <h3>Top Players</h3>
        </Col>
      </Row>
      <Row>
        <Col>
          <h3>Upcoming Games</h3>
          <ListGroup>
            {upcomingGames.map(game =>
              <ListGroup.Item>{game.game_number}</ListGroup.Item>
            )}
          </ListGroup>
        </Col>
        <Col></Col>
      </Row>
    </div>
  );
}

export default TeamOverview;
