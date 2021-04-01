import { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import Jumbotron from 'react-bootstrap/Jumbotron';

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
      <Jumbotron>
        <h1>{message}</h1>
      </Jumbotron>
      <Button disabled={isLoading} onClick={createLeague}>
        {isLoading ? 'Creating...' : 'Create A League'}
      </Button>
    </div>
  );
}

export default Home;
