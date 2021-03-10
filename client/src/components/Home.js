import { useState, useEffect } from 'react';

function Home() {
  const [message, setMessage] = useState('');
  useEffect(() => {
    setMessage("Welcome to baseball gm simulation")
  }, []);

  return (
    <div>
      <h1>HOME</h1>
      <p>{message}</p>
    </div>
  );
}

export default Home;
