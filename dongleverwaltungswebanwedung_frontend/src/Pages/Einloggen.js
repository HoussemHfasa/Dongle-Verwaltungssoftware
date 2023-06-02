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
  const navigate = useNavigate();

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
          "Anmeldung fehlgeschlagen. Bitte überprüfen Sie Ihre E-Mail und Passwort."
        );
      }
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.Background}>
        <div className={styles["white-rectangle"]} />

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
        <div className={styles["frame-text-Password"]}>Passwort</div>
        <input
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
        <div className={styles["frame-text-vergessen"]}>
          Passwort vergessen?
        </div>

        {/* Anmeldeknopf */}
        <button
          className={styles["rectangular-button"]}
          onClick={handleLoginSubmit}
        >
          Anmelden
        </button>

        <div className={styles["frame-overlap"]}></div>
      </div>

      {/* Fehlermeldung */}
      {errorMessage && (
        <div className={styles.error_message}>{errorMessage}</div>
      )}
    </div>
  );
};

export default Einloggen;
