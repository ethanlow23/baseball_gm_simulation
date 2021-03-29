import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Button from 'react-bootstrap/Button';

function Home() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    setMessage("Welcome to baseball gm simulation");
  }, []);

  const createLeague = (e) => {
    alert('I want to create a league');
  }

  return (
    <div>
      <h1>HOME</h1>
      <Button>{message}</Button>
      <Link to="/league" onClick={createLeague}>CREATE A LEAGUE</Link>
    </div>
  );
}

export default Home;
