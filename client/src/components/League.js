import { Switch, Route } from 'react-router-dom';
import LeagueTeams from './LeagueTeams';
import LeagueLeaders from './LeagueLeaders';
import LeagueStats from './LeagueStats';

function League() {
  return (
    <div>
      <h1>League</h1>
      <Switch>
        <Route path="/league/teams" component={LeagueTeams} />
        <Route path="/league/leaders" component={LeagueLeaders} />
        <Route path="/league/stats" component={LeagueStats} />
      </Switch>
    </div>
  );
}

export default League;
