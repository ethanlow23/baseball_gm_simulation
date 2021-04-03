import { useState, useEffect } from 'react';
import { Switch, Route, Link, useParams } from 'react-router-dom';
import PlayerStats from './PlayerStats';
import PlayerLog from './PlayerLog';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Nav from 'react-bootstrap/Nav';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Image from 'react-bootstrap/Image';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function Player() {
  const { player_id } = useParams();
  const [player, setPlayer] = useState({});
  const [years] = useState([2021, 2020]);

  useEffect(() => {
    fetch('/players/' + player_id)
      .then(response => response.json())
      .then(data => {setPlayer(data)})
      .catch(error => console.log(error));
  }, [player_id]);

  return (
    <div>
      <Jumbotron>
        <Row>
          <Col md={2}>
            <Image src="http://www.ltlondonfc.com/images/user-silhouette.png" Rounded width={200} height={210} />
          </Col>
          <Col md={10}>
            <h1>Player Information</h1>
            <h3>{player.first_name} {player.last_name}</h3>
          </Col>
        </Row>
      </Jumbotron>
      <Nav>
        <Nav.Link as={Link} to={"/player/" + player_id}>Player</Nav.Link>
        <Nav.Link as={Link} to={"/player/" + player_id + "/log"}>Game Log</Nav.Link>
        <Nav.Link as={Link} to={"/player/" + player_id + "/stats"}>Stats</Nav.Link>
        <NavDropdown title="2021">
          {years.map((year, i) => 
            <NavDropdown.Item key={i}>{year}</NavDropdown.Item>
          )}
        </NavDropdown>
      </Nav>
      <Switch>
        <Route path="/player/:player_id/log" component={PlayerLog} />
        <Route path="/player/:player_id/stats" component={PlayerStats} />
      </Switch>
    </div>
  );
}

export default Player;
