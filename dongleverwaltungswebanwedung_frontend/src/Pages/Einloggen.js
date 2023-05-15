import React, { useState } from "react";
import { Link } from "react-router-dom";
import styles from "./Einloggen.module.css";
import MyUsername from "./Username.png";
import MyPassword from "./Password.png";

const Einloggen = (props) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  return (
    <div className={styles.container}>
      <div className={styles.Background}>
        <div className={styles["white-rectangle"]} />
        <input
          type="text"
          placeholder="Schreiben Sie Ihr Benutzername"
          className={styles.textbox_Benutzername}
          onChange={(e) => setUsername(e.target.value)}
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
        <Link to="/Übersichtseite">
          <button className={styles["rectangular-button"]}>Anmelden</button>
        </Link>{" "}
        <div className={styles["frame-overlap"]}></div>
      </div>
    </div>
  );
};

export default Einloggen;
