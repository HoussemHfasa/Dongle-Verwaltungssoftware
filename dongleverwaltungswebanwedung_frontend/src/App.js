import logo from "./logo.svg";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Übersichtseite from "./Pages/Übersichtseite";
import Home from "./Pages/Einloggen";
import "./App.css";
import CAccount from "./Pages/CreateAccount/cAccount";

function App() {
  let component;

  switch (window.location.pathname) {
    case "/":
      component = <Home />;
      break;
    case "/Übersichtseite":
      component = <Übersichtseite />;
      break;
    case "/CreateAccount":
      component = <CAccount />;
      break;
    default:
      break;
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>React App</h1>
      </header>
      <main>
        {component}
      </main>
    </div>
  );
}

export default App;