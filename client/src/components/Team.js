import { useState, useEffect } from 'react';
import { Switch, Route, Link } from 'react-router-dom';
import TeamOverview from './TeamOverview';
import TeamSchedule from './TeamSchedule';
import TeamPlayers from './TeamPlayers';
import TeamStats from './TeamStats';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Nav from 'react-bootstrap/Nav';

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
      <Jumbotron>
        <h1>Team Information Page</h1>
        <h3>{team.city} {team.name}</h3>
      </Jumbotron>
      <Nav>
        <Nav.Link as={Link} to={"/team"}>Home</Nav.Link>
        <Nav.Link as={Link} to={"/team/schedule"}>Schedule</Nav.Link>
        <Nav.Link as={Link} to={"/team/players"}>Roster</Nav.Link>
        <Nav.Link as={Link} to={"/team/stats"}>Stats</Nav.Link>
      </Nav>
      <Switch>
        <Route path="/team" component={TeamOverview} exact />
        <Route path="/team/schedule" component={TeamSchedule} />
        <Route path="/team/players" component={TeamPlayers} />
        <Route path="/team/stats" component={TeamStats} />
      </Switch>
    </div>
  );
}

export default Team;
