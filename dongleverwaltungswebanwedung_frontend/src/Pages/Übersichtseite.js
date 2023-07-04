import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import styles from "./Übersichtseite.module.css";
import NavbarWrapper from "../Components/NavbarWrapper";
import DongleTable from "./DongleTable";
import { useAuth } from "../Components/AuthContext";

const Übersichtseite = () => {
  const navigate = useNavigate();
  const { email, password, role, last_login, setPassword } = useAuth();
  const [showPasswordChangePopup, setShowPasswordChangePopup] = useState(false);
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [showPopup, setShowPopup] = useState(false);
  const showSuccessPopup = () => {
    console.log("showSuccessPopup called");
    setShowPopup(true);
  };
  const SuccessPopup = () => (
    <div className={styles.popupWrapper}>
      <div className={styles.popup}>
        <p>Passwort erfolgreich geändert</p>
        <button
          className={styles.okButton}
          onClick={() => {
            navigate("/Übersichtseite");
            setShowPopup(false);
          }}
        >
          OK
        </button>
      </div>
      <div className={styles.overlay}></div>
    </div>
  );
  useEffect(() => {
    //Email in Lokalspeicher speichern
    localStorage.setItem("email", email);
  }, [email]);
  useEffect(() => {
    //Passwort in Lokalspeicher speichern
    localStorage.setItem("password", password);
  }, [password]);
  console.log("lastLogin :", last_login);
  useEffect(() => {
    const lastLogin = sessionStorage.getItem("last_login");
    console.log("lastLogin:", lastLogin); // Add this line

    if (!lastLogin || lastLogin === "null") {
      setShowPasswordChangePopup(true);
    }

    console.log("showPasswordChangePopup set to true"); // Add this line
  }, []);

  const handlePasswordChange = async (newPassword, confirmPassword) => {
    if (newPassword !== confirmPassword) {
      setErrorMessage("Die Passwörter stimmen nicht überein.");
      return;
    }

    try {
      const resetPasswordData = {
        email: email,
        oldPassword: password,
        newPassword: newPassword,
      };

      const response = await axios.post(
        "http://127.0.0.1:8000/passwortverwalten/",
        resetPasswordData
      );

      if (response.status === 200) {
        // Update the last_login value with the current date
        sessionStorage.setItem("last_login", new Date().toISOString());
        console.log(
          "Updated last_login:",
          sessionStorage.getItem("last_login")
        ); // Add this line
        showSuccessPopup();
        setPassword(newPassword);
        // Hide the password change popup
        setShowPasswordChangePopup(false);
      }
    } catch (error) {
      console.error("Error sending password:", error.message);
      if (error.response) {
        console.error("Server response data:", error.response.data);
        setErrorMessage("Fehler beim Ändern des Passworts.");
      }
    }
  };

  return (
    <div className={styles.container}>
      {/* Popup anzeigen, wenn showSuccessPopup wahr ist */}
      {showPopup && <SuccessPopup />}
      {/* Rahmen für Navbar und Hintergrund */}
      <div className={styles.frame7}>
        {/* Navbar */}
        <NavbarWrapper />
        {/* Rechteckiger Hintergrund */}
        <div className={styles.rectanglebackground}></div>
      </div>

      {/* Inhalt der Übersichtsseite */}
      <div className={styles.content}>
        {/* Dongle-Tabelle */}
        <div className={`${styles["DongleTable"]} ${styles.tableContainer}`}>
          {/* Neue CSS-Klasse hier hinzufügen */}
          <DongleTable />
        </div>

        {/* Dongle-Anforderungsbutton */}
        {/* ... Your Dongle-Anforderungsbutton code */}

        {showPasswordChangePopup && (
          <div className={styles.popupWrapper}>
            <div className={styles.password_change_popup}>
              <h2>Passwort ändern</h2>
              <p>
                Da dies Ihr erster Login ist, müssen Sie Ihr Passwort ändern,
                bevor Sie fortfahren können.
              </p>
              <input
                type="password"
                placeholder="Neues Passwort"
                onChange={(e) => setNewPassword(e.target.value)}
              />
              <input
                type="password"
                placeholder="Passwort bestätigen"
                onChange={(e) => setConfirmPassword(e.target.value)}
              />
              <button
                onClick={() =>
                  handlePasswordChange(newPassword, confirmPassword)
                }
              >
                Passwort ändern
              </button>
              {errorMessage && (
                <p className={styles.error_message}>{errorMessage}</p>
              )}
            </div>
            <div className={styles.overlay}></div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Übersichtseite;
