import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Einloggen.module.css";
import MyUsername from "./Username.png";
import MyPassword from "./Password.png";
import { useAuth } from "../Components/AuthContext";
import axios from "axios";

// Einloggen-Komponente
const Einloggen = () => {
  const { setRole, setEmail, setPassword, setFirmcode } = useAuth();
  const [inputEmail, setInputEmail] = useState("");
  const [inputPassword, setInputPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  /*const [emailInputKey, setEmailInputKey] = useState(0);*/
  const [passwordInputKey, setPasswordInputKey] = useState(0);
  const navigate = useNavigate();

  const handleOkClick = () => {
    setErrorMessage("");
    /*setInputEmail("");*/
    setInputPassword("");
    /*setEmailInputKey((prevKey) => prevKey + 1);*/
    setPasswordInputKey((prevKey) => prevKey + 1);
  };
  const handlePasswordResetClick = () => {
    navigate("/Passwortzurücksetzung");
  };

  // Verarbeitet das Einreichen des Login-Formulars
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
        localStorage.setItem("role", response.data.role);
        localStorage.setItem("Firmcode", response.data.firm_code);
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

  return (
    <div className={styles.container}>
      <div className={styles.Background}>
        <div className={styles["white-rectangle"]} />
        {/* Wrap input fields and the button with a form element */}
        <form onSubmit={handleLoginSubmit}>
          {/* E-Mail-Feld */}
          <input
            /* key={emailInputKey}*/
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
          <button
            className={styles["rectangular-button"]}
            type="submit" // Add type="submit" to the button
          >
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
