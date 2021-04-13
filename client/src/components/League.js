import { Switch, Route, Link } from 'react-router-dom';
import LeagueOverview from './LeagueOverview';
import LeagueTeams from './LeagueTeams';
import LeagueLeaders from './LeagueLeaders';
import LeagueStats from './LeagueStats';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Nav from 'react-bootstrap/Nav';

function League() {
  return (
    <div>
      <Jumbotron>
        <h1>League</h1>
      </Jumbotron>
      <Nav>
        <Nav.Link as={Link} to={"/league"}>Overview</Nav.Link>
        <Nav.Link as={Link} to={"/league/teams"}>Teams</Nav.Link>
        <Nav.Link as={Link} to={"/league/leaders"}>Leaders</Nav.Link>
        <Nav.Link as={Link} to={"/league/stats"}>Stats</Nav.Link>
      </Nav>
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
