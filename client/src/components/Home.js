import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Button from 'react-bootstrap/Button';

function Home() {
  const [message, setMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const simulateNetworkRequest = () => {
    return new Promise ((resolve) => setTimeout(resolve, 5000));
  };

  useEffect(() => {
    setMessage("Welcome to baseball gm simulation");
    if (isLoading) {
      simulateNetworkRequest().then(() => setIsLoading(false));
    };
  }, [isLoading]);

  const createLeague = (e) => setIsLoading(true);

  return (
    <div>
      <h1>{message}</h1>
      <Button disabled={isLoading} onClick={createLeague}>
        {isLoading ? 'Creating...' : 'Create A League'}
      </Button>
    </div>
  );
}

export default Home;
