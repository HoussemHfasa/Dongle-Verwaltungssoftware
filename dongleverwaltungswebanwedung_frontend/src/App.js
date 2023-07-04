import React from "react";
import { AuthProvider } from "./Components/AuthContext";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Uebersichtseite from "./Pages/Übersichtseite";
import LizenUebersicht from "./Pages/Lizenübersicht";
import Einloggen from "./Pages/Einloggen";
import Adminseite from "./Pages/Adminseite";
import "./App.css";
import Donglehinzufuegen from "./Pages/Donglehinzufuegen";
import Kontoerstellen from "./Pages/Kontoerstellen";
import Profileseite from "./Pages/Profileseite";
import PasswortZuruecksetzung from "./Pages/Passwortzurücksetzung";
import LizenzHinzufuegen from "./Pages/Lizenzhinzufügen";
import LizenzAnfordern from "./Pages/LizenzAnfordern";
import Lizenzanfordernantwort from "./Pages/Lizenzanfordernantwort";

function App() {
  return (
    <AuthProvider>
      <div className="App">
        <main>
          <Router>
            <Routes>
              <Route path="/" element={<Einloggen />} />
              <Route path="/Übersichtseite" element={<Uebersichtseite />} />

              <Route
                path="/Donglehinzufuegen"
                element={<Donglehinzufuegen />}
              />
              <Route path="/Lizenübersicht" element={<LizenUebersicht />} />
              <Route
                path="/Lizenzanfordernantwort"
                element={<Lizenzanfordernantwort />}
              />
              <Route path="/Admin" element={<Adminseite />} />
              <Route path="/Kontoerstellen" element={<Kontoerstellen />} />
              <Route path="/Profileseite" element={<Profileseite />} />
              <Route
                path="/Lizenzhinzufuegen"
                element={<LizenzHinzufuegen />}
              />
              <Route
                path="/Passwortzurücksetzung"
                element={<PasswortZuruecksetzung />}
              />
              <Route path="/LizenzAnfordern" element={<LizenzAnfordern />} />
            </Routes>
          </Router>
        </main>
      </div>
    </AuthProvider>
  );
}

export default App;
