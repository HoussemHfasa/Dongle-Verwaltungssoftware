import logo from "./logo.svg";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Übersichtseite from "./Pages/Übersichtseite";
import Home from "./Pages/Einloggen";
import "./App.css";
import Kunde_Dongle_anfordern from "./Pages/Kunde_Dongle_anfordern/Kunde_Dongle_anfordern";

function App() {
  let component;

  switch (window.location.pathname) {
    case "/":
      component = <Home />;
      break;
    case "/Übersichtseite":
      component = <Übersichtseite />;
      break;
    case "/Kunde_Dongle_anfordern":
      component = <Kunde_Dongle_anfordern />;
      break;
    default:
      break;
  }

  return (
    <div className="App">
      <div className="App">
        <header className="App-header">
          <h1>React App</h1>
        </header>
        <main>
          <Übersichtseite />
        </main>
      </div>
    </div>
  );
}
export default App;
