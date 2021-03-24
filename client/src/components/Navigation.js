import { Link } from 'react-router-dom';

function Navigation () {
  const simGames = (e) => {
    alert('I want to simulate games');
  }
  return (
    <div>
      <h1>Navigation Bar</h1>
      <button onClick={simGames}>Play</button>
      <div>
        <Link to="/">Dashboard</Link>
      </div>
      <div>
        <Link to="/league">League</Link>
        <Link to="/league/teams">Teams</Link>
        <Link to="/league/leaders">League Leaders</Link>
        <Link to="/league/stats">Team Stats</Link>
      </div>
      <div>
        <Link to="/team">My Team</Link>
        <Link to="/team/schedule">Schedule</Link>
        <Link to="/team/players">Roster</Link>
        <Link to="/team/stats">Team Stats</Link>
      </div>
    </div>
  );
}

export default Navigation;
