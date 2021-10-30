import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import Navbar from "./components/navbar";
import HomePage from "./pages/HomePage";
import LoginPage from "./pages/Login";
import SignupPage from "./pages/Signup";


const App = () => {
  return <>
    <Router>
      <Navbar />

      <Switch>
        <Route path="/" exact component={HomePage} />
        <Route path="/login" exact component={LoginPage} />
        <Route path="/signup" exact component={SignupPage} />
      </Switch>

    </Router>
  </>
};

export default App;
