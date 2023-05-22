import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Einloggen from "./Pages/Einloggen";
import Übersichtseite from "./Pages/Übersichtseite";
import DongleAnfordern from "./Pages/DongleAnfordern";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<Einloggen />} />
        <Route path="/Übersichtseite" element={<Übersichtseite />} />
        <Route path="/DongleAnfordern" element={<DongleAnfordern />} />
      </Routes>
    </Router>
  </React.StrictMode>
);

reportWebVitals();
