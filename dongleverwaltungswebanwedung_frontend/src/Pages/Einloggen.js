import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Einloggen.module.css";
import MyUsername from "./Username.png";
import MyPassword from "./Password.png";
import { useAuth } from "../Components/AuthContext"; // Import the useAuth hook

const Einloggen = () => {
  const { setUsername } = useAuth();
  const [inputUsername, setInputUsername] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();

    if (
      inputUsername === "admin" ||
      inputUsername === "Admin" ||
      inputUsername === "verwalter" ||
      inputUsername === "Verwalter" ||
      inputUsername === "kunde" ||
      inputUsername === "Kunde"
    ) {
      setUsername(inputUsername); // Update the global state with the username
      navigate("/Übersichtseite");
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.Background}>
        <div className={styles["white-rectangle"]} />
        <input
          type="text"
          placeholder="Schreiben Sie Ihr Benutzername"
          className={styles.textbox_Benutzername}
          onChange={(e) => setInputUsername(e.target.value)}
        />
        <div className={styles["frame-Benutzername"]}>Benutzername</div>
        <div className={styles["frame-text-Benutzername"]}>
          Schreiben Sie Ihr Benutzername
        </div>
        <img
          className={styles["frame-image-Username"]}
          alt="MyUsername"
          src={MyUsername}
        />
        <div className={styles["frame-text-Password"]}>Passwort</div>
        <input
          type="text"
          placeholder="Schreiben Sie Ihr Passwort"
          className={styles.textbox_Passwort}
          onChange={(e) => setPassword(e.target.value)}
        />
        <img
          className={styles["frame-image-Password"]}
          alt="MyPassword"
          src={MyPassword}
        />
        <div className={styles["frame-text-vergessen"]}>
          Passwort vergessen?
        </div>
        <button className={styles["rectangular-button"]} onClick={handleLogin}>
          Anmelden
        </button>
        <div className={styles["frame-overlap"]}></div>
      </div>
    </div>
  );
};

export default Einloggen;
