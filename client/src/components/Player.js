import { useState, useEffect } from 'react';
import { Switch, Route, Link, useParams } from 'react-router-dom';
import PlayerLog from './PlayerLog';
import Jumbotron from 'react-bootstrap/Jumbotron';

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
      <Link to={"/player/" + player_id}>Player</Link>
      <Link to={"/player/" + player_id + "/log"}>Game Log</Link>
      <Link to={"/player/" + player_id + "/log"}>Stats</Link>
      <Switch>
        <Route path="/player/:player_id/log" component={PlayerLog} />
      </Switch>
    </div>
  );
}

export default Player;
