import logo from "./logo.svg";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Einloggen from "./Pages/Einloggen";
import Übersichtseite from "./Pages/Übersichtseite";
import { Home } from "./Pages/Home";
import "./App.css";

function App() {
  let component;
  switch (window.location.pathname) {
    case "/":
      component = <Home />;
      break;
    case "/Übersichtseite":
      component = <Übersichtseite />;
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
