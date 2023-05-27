import React from "react";
import { AuthProvider } from "./Components/AuthContext";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Übersichtseite from "./Pages/Übersichtseite";
import Lizensüberscht from "./Pages/Lizenübersicht";
import Einloggen from "./Pages/Einloggen";
import "./App.css";
import DongleAnfordern from "./Pages/DongleAnfordern";

function App() {
  return (
    <AuthProvider>
      <div className="App">
        <main>
          <Router>
            <Routes>
              <Route path="/" element={<Einloggen />} />
              <Route path="/Übersichtseite" element={<Übersichtseite />} />
              <Route path="/DongleAnfordern" element={<DongleAnfordern />} />
              <Route path="/Lizenübersicht" element={<Lizensüberscht />} />
            </Routes>
          </Router>
        </main>
      </div>
    </AuthProvider>
  );
}

export default App;
