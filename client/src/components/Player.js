import { useState, useEffect } from 'react';
import { Switch, Route, Link } from 'react-router-dom';
import PlayerLog from './PlayerLog';

function Player() {
  const [player, setPlayer] = useState({});

  useEffect(() => {
    fetch('/players/1')
      .then(response => response.json())
      .then(data => {setPlayer(data)})
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>Player Information</h1>
      <Link to="/player/log">Game Log</Link>
      <p>{player.first_name} {player.last_name}</p>
      <Switch>
        <Route path="/player/log" component={PlayerLog} />
      </Switch>
    </div>
  );
}

export default Player;
