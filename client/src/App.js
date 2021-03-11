import { Switch, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import Home from './components/Home';
import League from './components/League';
import Team from './components/Team';

function App() {
  return (
    <div className="App">
      <Navigation />
      <Switch>
        <Route path="/" component={Home} exact />
        <Route path="/league" component={League} />
        <Route path="/team" component={Team} />
      </Switch>
    </div>
  );
}

export default App;
