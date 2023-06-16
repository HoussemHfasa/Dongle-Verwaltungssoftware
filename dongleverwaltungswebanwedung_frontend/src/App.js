import React from "react";
import { AuthProvider } from "./Components/AuthContext";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Übersichtseite from "./Pages/Übersichtseite";
import Lizensüberscht from "./Pages/Lizenübersicht";
import Einloggen from "./Pages/Einloggen";
import Adminseite from "./Pages/Adminseite";
import "./App.css";
import Donglehinzufuegen from "./Pages/Donglehinzufuegen";
import Kontoerstellen from "./Pages/Kontoerstellen";
import Profileseite from "./Pages/Profileseite";
import Passwortzurücksetzung from "./Pages/Passwortzurücksetzung";
import Lizenzhinzufuegen from "./Pages/Lizenzhinzufügen";

function App() {
  return (
    <AuthProvider>
      <div className="App">
        <main>
          <Router>
            <Routes>
              <Route path="/" element={<Einloggen />} />
              <Route path="/Übersichtseite" element={<Übersichtseite />} />

              <Route
                path="/Donglehinzufuegen"
                element={<Donglehinzufuegen />}
              />
              <Route path="/Lizenübersicht" element={<Lizensüberscht />} />
              <Route path="/Admin" element={<Adminseite />} />
              <Route path="/Kontoerstellen" element={<Kontoerstellen />} />
              <Route path="/Profileseite" element={<Profileseite />} />
              <Route
                path="/Lizenzhinzufuegen"
                element={<Lizenzhinzufuegen />}
              />
              <Route
                path="/Passwortzurücksetzung"
                element={<Passwortzurücksetzung />}
              />
            </Routes>
          </Router>
        </main>
      </div>
    </AuthProvider>
  );
}

export default App;
