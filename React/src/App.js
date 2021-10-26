import './App.css'
import './index.css'
import { Route } from 'react-router-dom'
import Home from './Components/Home'
import CotReport from './Components/CotReport'
import Login from './Components/Login'
import CreateAccount from './Components/CreateAccount'
import Profile from './Components/Profile'


function App() {

  return (
    <div className="App">
      <Route exact path="/cot-tails" component={Home}/>
      <Route path="/report" component={CotReport}/>
      <Route path="/login" component={Login}/>
      <Route path="/create-account" component={CreateAccount}/>
      <Route path="/profile" component={Profile}/>
    </div>
  );
}

export default App;
