import { Link } from 'react-router-dom';
import { Navbar, Nav, NavDropdown, Button } from 'react-bootstrap';

function Navigation () {
  const simGames = (e) => {
    fetch('/simulate', {method: 'POST'})
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.log(error))
  };
  
  return (
    <div>
      <Navbar bg="light" expand="lg">
        <Navbar.Brand>Baseball GM Simulator</Navbar.Brand>
          <Nav>
            <Button onClick={simGames}>Play</Button>
            <Nav.Link as={Link} to="/">Dashboard</Nav.Link>
            <NavDropdown title="League">
              <NavDropdown.Item as={Link} to="/league">Overview</NavDropdown.Item>
              <NavDropdown.Item as={Link} to="/league/teams">Teams</NavDropdown.Item>
              <NavDropdown.Item as={Link} to="/league/leaders">League Leaders</NavDropdown.Item>
              <NavDropdown.Item as={Link} to="/league/stats">Stats</NavDropdown.Item>
            </NavDropdown>
            <NavDropdown title="Team">
              <NavDropdown.Item as={Link} to="/team">My Team</NavDropdown.Item>
              <NavDropdown.Item as={Link} to="/team/schedule">Schedule</NavDropdown.Item>
              <NavDropdown.Item as={Link} to="/team/players">Roster</NavDropdown.Item>
              <NavDropdown.Item as={Link} to="/team/stats">Team Stats</NavDropdown.Item>
            </NavDropdown>
          </Nav>
      </Navbar>
    </div>
  );
}

export default Navigation;
