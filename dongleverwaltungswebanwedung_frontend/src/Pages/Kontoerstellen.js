import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import NavbarWrapper from "../Components/NavbarWrapper";
import styles from "./Kontoerstellen.module.css";
import { useAuth } from "../Components/AuthContext";
import useAdminAccess from "./useAdminAccess";

const Kontoerstellen = () => {
  // Navigation
  const navigate = useNavigate();

  // Zustände für Eingabefelder
  const [role1, setRole1] = useState("");
  const [email1, setEmail1] = useState("");
  const [confirmEmail, setConfirmEmail] = useState("");
  const [name1, setName1] = useState("");
  const [firmCode, setFirmCode] = useState("");

  // Authentifizierung
  const { email, password } = useAuth();
  const { isAdmin, isLoading } = useAdminAccess();

  // Funktion zum Überprüfen, ob Eingabe nur Leerzeichen enthält
  const isInputOnlySpaces = (input) => {
    return /^\s*$/.test(input);
  };

  // Effekte für die Speicherung von E-Mail und Passwort im localStorage
  useEffect(() => {
    localStorage.setItem("email", email);
  }, [email]);
  useEffect(() => {
    localStorage.setItem("password", password);
  }, [password]);

  // Weiterleitung zur Übersichtseite, wenn Benutzer kein Admin ist
  useEffect(() => {
    if (!isLoading && !isAdmin) {
      console.log("isAdmin:", isAdmin);
      navigate("/Übersichtseite");
    }
  }, [isAdmin, navigate, isLoading]);

  // Popup für erfolgreiche Erstellung eines neuen Benutzers
  const [showPopup, setShowPopup] = useState(false);
  const showSuccessPopup = () => {
    setShowPopup(true);
  };
  const SuccessPopup = () => (
    <div className={styles.popupWrapper}>
      <div className={styles.popup}>
        <p>Neuer Benutzer erstellt</p>
        <button className={styles.okButton} onClick={() => navigate("/Admin")}>
          OK
        </button>
      </div>
    </div>
  );

  // Funktion zum Überprüfen, ob E-Mail-Adresse gültig ist
  const isEmailValid = (emailAddress) => {
    const emailRegex = /^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/;
    return emailRegex.test(emailAddress);
  };

  // Überprüfung der Gültigkeit des Formulars
  const isFormValid =
    role1 &&
    isEmailValid(email1) &&
    !isInputOnlySpaces(email1) &&
    email1 === confirmEmail &&
    !isInputOnlySpaces(name1) &&
    name1 &&
    (role1 !== "Kunde" || (firmCode && !isInputOnlySpaces(firmCode)));

  // Funktion zum Abrufen des Admin-Zugriffstokens
  const getAdminAccessToken = async () => {
    try {
      console.log(email, password);
      const response = await axios.post(
        "http://127.0.0.1:8000/admin-access-token/",
        {
          email: email,
          password: password,
        }
      );

      if (response.status === 200) {
        return response.data.access_token;
      }
    } catch (error) {
      console.error("Error obtaining admin access token:", error.message);
      if (error.response) {
        console.error("Server response data:", error.response.data);
      }
    }

    return null;
  };

  // Formular-Handler zum Erstellen eines neuen Benutzers
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (isFormValid) {
      const newUser = {
        email: email1,
        name: name1,
        role: role1,
        firm_code: firmCode,
      };

      try {
        const adminAccessToken = await getAdminAccessToken();
        if (!adminAccessToken) {
          console.error("Failed to obtain admin access token");
          return;
        }

        const response = await axios.post(
          "http://127.0.0.1:8000/users/",
          newUser,
          {
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${adminAccessToken}`,
            },
          }
        );

        if (response.status === 201) {
          console.log("New user created:", response.data);
          showSuccessPopup();
        }
      } catch (error) {
        console.error("Error creating user:", error.message);
        if (error.response) {
          console.error("Server response data:", error.response.data);
        }
      }
    }
  };

  // Render-Funktion für das Kontoerstellen-Formular
  return (
    <div className={styles.wrapper}>
      {showPopup && <SuccessPopup />}
      <div className={styles.container}>
        {/* Rahmen für Navbar und Hintergrund */}
        <div className={styles.frame7}>
          {/* Navbar */}
          <NavbarWrapper />
          {/* Rechteckiger Hintergrund */}
          <div className={styles.rectanglebackground}></div>
        </div>
        <form onSubmit={handleSubmit}>
          <div className={styles.inputContainer}>
            {/* Rollenauswahl */}
            <select value={role1} onChange={(e) => setRole1(e.target.value)}>
              <option value="">Rolle wählen</option>
              <option value="Admin">Admin</option>
              <option value="Verwalter">Verwalter</option>
              <option value="Kunde">Kunde</option>
            </select>
            {/* E-Mail-Eingabe */}
            <input
              type="email"
              placeholder="E-Mail"
              value={email1}
              onChange={(e) => setEmail1(e.target.value)}
            />
            {/* E-Mail-Bestätigung */}
            <input
              type="email"
              placeholder="E-Mail bestätigen"
              value={confirmEmail}
              onChange={(e) => setConfirmEmail(e.target.value)}
            />
            {/* Name-Eingabe */}
            <input
              type="text"
              placeholder="Name"
              value={name1}
              onChange={(e) => setName1(e.target.value)}
            />
            {/* Firmencode-Eingabe, nur wenn Rolle "Kunde" */}
            {role1 === "Kunde" && (
              <input
                type="text"
                placeholder="Firmencode"
                value={firmCode}
                onChange={(e) => setFirmCode(e.target.value)}
              />
            )}
            {/* Benutzer erstellen-Button */}
            <button
              className={styles.createAccountBtn}
              type="submit"
              disabled={!isFormValid}
            >
              Benutzer erstellen
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Kontoerstellen;
