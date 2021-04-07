import { useState, useEffect } from 'react';
import { Switch, Route, Link, useParams } from 'react-router-dom';
import TeamOverview from './TeamOverview';
import TeamSchedule from './TeamSchedule';
import TeamPlayers from './TeamPlayers';
import TeamStats from './TeamStats';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Nav from 'react-bootstrap/Nav';

function Team() {
  const { team_id } = useParams();
  const [team, setTeam] = useState({});

  useEffect(() => {
    fetch('/teams/' + team_id)
      .then(response => response.json())
      .then(data => setTeam(data))
      .catch(error => console.log(error));
  }, [team_id]);

  return (
    <div>
      <Jumbotron>
        <h1>Team Information Page</h1>
        <h3>{team.city} {team.name}</h3>
      </Jumbotron>
      <Nav>
        <Nav.Link as={Link} to={"/team/" + team_id}>Home</Nav.Link>
        <Nav.Link as={Link} to={"/team/" + team_id + "/schedule"}>Schedule</Nav.Link>
        <Nav.Link as={Link} to={"/team/" + team_id + "/players"}>Roster</Nav.Link>
        <Nav.Link as={Link} to={"/team/" + team_id + "/stats"}>Stats</Nav.Link>
      </Nav>
      <Switch>
        <Route path="/team/:team_id" component={TeamOverview} exact />
        <Route path="/team/:team_id/schedule" component={TeamSchedule} />
        <Route path="/team/:team_id/players" component={TeamPlayers} />
        <Route path="/team/:team_id/stats" component={TeamStats} />
      </Switch>
    </div>
  );
}

export default Team;
