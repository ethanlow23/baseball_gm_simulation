import { useState, useEffect } from 'react';
import { Switch, Route } from 'react-router-dom';
import TeamSchedule from './TeamSchedule';
import TeamPlayers from './TeamPlayers';
import TeamStats from './TeamStats';

function Team() {
  const [team, setTeam] = useState({});

  useEffect(() => {
    fetch('/teams/1')
      .then(response => response.json())
      .then(data => setTeam(data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>Team Information Page</h1>
      <h3>{team.city} {team.name}</h3>
      <Switch>
        <Route path="/team/schedule" component={TeamSchedule} />
        <Route path="/team/players" component={TeamPlayers} />
        <Route path="/team/stats" component={TeamStats} />
      </Switch>
    </div>
  );
}

export default Team;
