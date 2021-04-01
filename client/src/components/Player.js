import { useState, useEffect } from 'react';
import { Switch, Route, Link, useParams } from 'react-router-dom';
import PlayerStats from './PlayerStats';
import PlayerLog from './PlayerLog';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Nav from 'react-bootstrap/Nav';

function Player() {
  const { player_id } = useParams();
  const [player, setPlayer] = useState({});

  useEffect(() => {
    fetch('/players/' + player_id)
      .then(response => response.json())
      .then(data => {setPlayer(data)})
      .catch(error => console.log(error));
  }, [player_id]);

  return (
    <div>
      <Jumbotron>
        <h1>Player Information</h1>
        <h3>{player.first_name} {player.last_name}</h3>
      </Jumbotron>
      <Nav>
        <Nav.Item><Nav.Link as={Link} to={"/player/" + player_id}>Player</Nav.Link></Nav.Item>
        <Nav.Item><Nav.Link as={Link} to={"/player/" + player_id + "/log"}>Game Log</Nav.Link></Nav.Item>
        <Nav.Item><Nav.Link as={Link} to={"/player/" + player_id + "/stats"}>Stats</Nav.Link></Nav.Item>
      </Nav>
      <Switch>
        <Route path="/player/:player_id/log" component={PlayerLog} />
        <Route path="/player/:player_id/stats" component={PlayerStats} />
      </Switch>
    </div>
  );
}

export default Player;
