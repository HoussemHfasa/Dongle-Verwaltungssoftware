import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Einloggen.module.css";
import MyUsername from "./Username.png";
import MyPassword from "./Password.png";
import { useAuth } from "../Components/AuthContext";
import axios from "axios"; // Import axios

const Einloggen = () => {
  const { setRole, setEmail, setPassword, handleLogin } = useAuth(); // Add setRole here
  const [inputEmail, setInputEmail] = useState(""); // Add back the local state variable for email input
  const [inputPassword, setInputPassword] = useState(""); // Add back the local state variable for password input
  const [errorMessage, setErrorMessage] = useState("");

  const navigate = useNavigate();

  const handleLoginSubmit = async (e) => {
    e.preventDefault();

    try {
      // Send a POST request to the API with the user's email and password
      const response = await axios.post("http://localhost:8000/login/", {
        email: inputEmail, // Use inputEmail instead of this.state.email
        password: inputPassword, // Use inputPassword instead of this.state.password
      });
      if (response.status === 200) {
        setRole(response.data.role); // Update the global state with the role
        setEmail(inputEmail); // Update the global email state
        setPassword(inputPassword); // Update the global password state
        console.log("Role, email, and password set successfully"); // Log a message to check if this part of code is executed
        navigate("/Übersichtseite");
      }
    } catch (error) {
      console.error("Login failed:", error.message);
      if (error.response) {
        console.error("Server response data:", error.response.data);
        setErrorMessage(
          "Login fehlgeschlagen. Bitte überprüfen Sie Ihre E-Mail und Passwort."
        );
      }
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.Background}>
        <div className={styles["white-rectangle"]} />
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
        <div className={styles["frame-text-vergessen"]}>
          Passwort vergessen?
        </div>
        <button
          className={styles["rectangular-button"]}
          onClick={handleLoginSubmit}
        >
          Anmelden
        </button>
        <div className={styles["frame-overlap"]}></div>
      </div>
      {errorMessage && (
        <div className={styles.error_message}>{errorMessage}</div>
      )}
    </div>
  );
};

export default Einloggen;
