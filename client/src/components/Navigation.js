import { Link } from 'react-router-dom';

function Navigation () {
  return (
    <div>
      <h1>Navigation Bar</h1>
      <Link to="/">Dashboard</Link>
      <Link to="/league">League</Link>
      <Link to="/team">My Team</Link>
      <Link to="/stats">Stats</Link>
    </div>
  );
}

export default Navigation;
