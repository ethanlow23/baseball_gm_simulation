import { Link } from 'react-router-dom';

function Navigation () {
  const simGames = (e) => {
    alert('I want to simulate games');
  }
  return (
    <div>
      <h1>Navigation Bar</h1>
      <button onClick={simGames}>Play</button>
      <Link to="/">Dashboard</Link>
      <Link to="/league">League</Link>
      <Link to="/team">My Team</Link>
      <Link to="/team/schedule">Schedule</Link>
      <Link to="/team/players">Roster</Link>
      <Link to="/team/stats">Team Stats</Link>
    </div>
  );
}

export default Navigation;
