import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Einloggen from "./Pages/Einloggen";
import Kunde_Dongle_anfordern from "./Pages/Kunde_Dongle_anfordern/Kunde_Dongle_anfordern";

import Übersichtseite from "./Pages/Übersichtseite";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Einloggen />,
  },
  {
    path: "/Übersichtseite",
    element: <Übersichtseite />,
  },
  {
    path: "/Kunde_Dongle_anfordern",
    element: <Kunde_Dongle_anfordern />,
  },
]);
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<RouterProvider router={router} />);
/*
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Einloggen />
  </React.StrictMode>
);*/

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
/*
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<RouterProvider router={router} />);
*/
