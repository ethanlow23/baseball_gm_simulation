import { Switch, Route } from 'react-router-dom';
import LeagueOverview from './LeagueOverview';
import LeagueTeams from './LeagueTeams';
import LeagueLeaders from './LeagueLeaders';
import LeagueStats from './LeagueStats';
import Jumbotron from 'react-bootstrap/Jumbotron';

function League() {
  return (
    <div>
      <Jumbotron>
        <h1>League</h1>
      </Jumbotron>
      <Switch>
        <Route path="/league" component={LeagueOverview} exact />
        <Route path="/league/teams" component={LeagueTeams} />
        <Route path="/league/leaders" component={LeagueLeaders} />
        <Route path="/league/stats" component={LeagueStats} />
      </Switch>
    </div>
  );
}

export default League;
