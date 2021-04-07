import { Switch, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import Home from './components/Home';
import League from './components/League';
import Team from './components/Team';
import Player from './components/Player';
import Game from './components/Game';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">
      <Navigation />
      <Switch>
        <Route path="/" component={Home} exact />
        <Route path="/league" component={League} />
        <Route path="/team/:team_id" component={Team} />
        <Route path="/player/:player_id" component={Player} />
        <Route path="/game/:game_id" component={Game} />
      </Switch>
    </div>
  );
}

export default App;
