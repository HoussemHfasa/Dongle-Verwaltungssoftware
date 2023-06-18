import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Einloggen.module.css";
import MyUsername from "../Pictures/Username.png";
import MyPassword from "../Pictures/Password.png";
import { useAuth } from "../Components/AuthContext";
import axios from "axios";

// Einloggen-Komponente
const Einloggen = () => {
  // Verwenden von useAuth für Authentifizierungszwecke
  const { setRole, setEmail, setPassword, setFirmcode, role } = useAuth();

  // Verwenden von useState für lokale Zustandsverwaltung
  const [inputEmail, setInputEmail] = useState("");
  const [inputPassword, setInputPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [passwordInputKey, setPasswordInputKey] = useState(0);

  // Verwenden von useNavigate für die Navigation zwischen den Seiten
  const navigate = useNavigate();

  // Verwenden von useEffect, um den Benutzer zur Übersichtsseite weiterzuleiten, wenn er bereits angemeldet ist
  useEffect(() => {
    if (role === "Admin" || role === "Verwalter" || role === "Kunde") {
      console.log("User is already logged in, redirecting...");
      navigate("/Übersichtseite");
    }
  }, [role, navigate]);

  // Funktion zum Zurücksetzen des Passworts und der Fehlermeldung
  const handleOkClick = () => {
    setErrorMessage("");
    setInputPassword("");
    setPasswordInputKey((prevKey) => prevKey + 1);
  };

  // Funktion zum Navigieren zur Passwortzurücksetzungsseite
  const handlePasswordResetClick = () => {
    navigate("/Passwortzurücksetzung");
  };

  // Funktion zum Verarbeiten des Einreichens des Login-Formulars
  const handleLoginSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://localhost:8000/login/", {
        email: inputEmail,
        password: inputPassword,
      });

      if (response.status === 200) {
        setRole(response.data.role);
        setFirmcode(response.data.firm_code);
        setEmail(inputEmail);
        setPassword(inputPassword);
        sessionStorage.setItem("role", response.data.role);
        sessionStorage.setItem("Firmcode", response.data.firm_code);
        sessionStorage.setItem("email", inputEmail);
        sessionStorage.setItem("password", inputPassword);
        console.log("Firmcode:", response.data.firm_code);
        console.log("Rolle, E-Mail und Passwort erfolgreich gesetzt");
        navigate("/Übersichtseite");
      }
    } catch (error) {
      console.error("Anmeldung fehlgeschlagen:", error.message);
      if (error.response) {
        console.error("Server-Antwortdaten:", error.response.data);
        setErrorMessage(
          "Anmeldung fehlgeschlagen. Bitte überprüfen Sie Ihre E-Mail oder Passwort."
        );
      }
    }
  };

  // Rückgabe der Einloggen-Komponente
  return (
    <div className={styles.container}>
      <div className={styles.Background}>
        <div className={styles["white-rectangle"]} />
        {/* Wrap input fields and the button with a form element */}
        <form onSubmit={handleLoginSubmit}>
          {/* E-Mail-Feld */}
          <input
            type="text"
            placeholder="Schreiben Sie Ihr E-Mail"
            className={styles.textbox_Benutzername}
            onChange={(e) => setInputEmail(e.target.value)}
          />
          <div className={styles["frame-Benutzername"]}>E-Mail</div>
          <div className={styles["frame-text-Benutzername"]}>
            Schreiben Sie Ihr Benutzername
          </div>
          <img
            className={styles["frame-image-Username"]}
            alt="MyUsername"
            src={MyUsername}
          />

          {/* Passwort-Feld */}
          <input
            key={passwordInputKey}
            type="password"
            placeholder="Schreiben Sie Ihr Passwort"
            className={styles.textbox_Passwort}
            onChange={(e) => setInputPassword(e.target.value)}
          />
          <div className={styles["frame-Passwort"]}>Passwort</div>
          <div className={styles["frame-text-Password"]}></div>
          <img
            className={styles["frame-image-Password"]}
            alt="MyPassword"
            src={MyPassword}
          />

          {/* Passwort-vergessen-Link */}
          <button
            type="button"
            className={styles["frame-text-vergessen"]}
            onClick={handlePasswordResetClick}
          >
            Passwort vergessen ?
          </button>

          {/* Anmeldeknopf */}
          <button className={styles["rectangular-button"]} type="submit">
            Anmelden
          </button>
        </form>
        <div className={styles["frame-overlap"]}></div>
      </div>

      {/* Fehlermeldung */}
      {errorMessage && (
        <div className={styles.popup_error_message}>
          {errorMessage}
          <button className={styles.ok_button} onClick={handleOkClick}>
            OK
          </button>
        </div>
      )}
    </div>
  );
};

export default Einloggen;
