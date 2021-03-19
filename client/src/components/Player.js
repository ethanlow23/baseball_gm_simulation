import { useState, useEffect } from 'react';
import { Switch, Route, Link, useParams } from 'react-router-dom';
import PlayerLog from './PlayerLog';

function Player() {
  const { player_id } = useParams();
  const [player, setPlayer] = useState({});

  useEffect(() => {
    fetch('/players/' + player_id)
      .then(response => response.json())
      .then(data => {setPlayer(data)})
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>Player Information</h1>
      <Link to={"/player/" + player_id + "/log"}>Game Log</Link>
      <p>{player.first_name} {player.last_name}</p>
      <Switch>
        <Route path="/player/:player_id/log" component={PlayerLog} />
      </Switch>
    </div>
  );
}

export default Player;
