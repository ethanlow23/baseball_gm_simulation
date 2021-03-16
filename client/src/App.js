import { Switch, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import Home from './components/Home';
import League from './components/League';
import Team from './components/Team';
import Player from './components/Player';
import Game from './components/Game';

function App() {
  return (
    <div className="App">
      <Navigation />
      <Switch>
        <Route path="/" component={Home} exact />
        <Route path="/league" component={League} />
        <Route path="/team" component={Team} />
        <Route path="/player" component={Player} />
        <Route path="/game" component={Game} />
      </Switch>
    </div>
  );
}

export default App;
