import React from "react";
import { AuthProvider } from "./Components/AuthContext";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Übersichtseite from "./Pages/Übersichtseite";
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
            </Routes>
          </Router>
        </main>
      </div>
    </AuthProvider>
  );
}

export default App;
