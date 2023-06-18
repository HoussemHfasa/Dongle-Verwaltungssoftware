import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import NavbarWrapper from "../Components/NavbarWrapper";
import styles from "./Profileseite.module.css";
import { useAuth } from "../Components/AuthContext";

const Profileseite = () => {
  const navigate = useNavigate();
  const [oldPassword, setOldPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmNewPassword, setConfirmNewPassword] = useState("");
  const [isFormValid, setIsFormValid] = useState(false);
  const { email, password, setPassword } = useAuth();
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
          onClick={() => navigate("/Übersichtseite")}
        >
          OK
        </button>
      </div>
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

  const checkFormValidity = (
    currentOldPassword,
    currentNewPassword,
    currentConfirmNewPassword
  ) => {
    //Überprüfen, ob das Formular gültig ist
    setIsFormValid(
      currentOldPassword === password &&
        currentNewPassword.trim() !== "" &&
        currentNewPassword === currentConfirmNewPassword
    );
  };
  const getUserAccessToken = async () => {
    //Benutzerzugriffstoken abrufen
    try {
      console.log(email, password);
      const response = await axios.post(
        "http://127.0.0.1:8000/user-access-token/",
        {
          email: email,
          password: password,
        }
      );
      if (response.status === 200) {
        return response.data.access_token;
      }
    } catch (error) {
      //Fehlerbehandlung
      console.error("Error obtaining user access token:", error.message);
      if (error.response) {
        console.error("Server response data:", error.response.data);
      }
    }
    return null;
  };
  const handleSubmit = async (e) => {
    //Passwort ändern
    e.preventDefault();
    if (isFormValid) {
      const newUser = {
        //Neuer Benutzer
        email: email,
        oldPassword: password,
        newPassword: newPassword,
      };
      console.log({
        //Alte und neue Passwörter sowie E-Mail protokollieren
        "old password: ": oldPassword,
        "new password:": newPassword,
        "Email :": email,
      });

      try {
        const userAccessToken = await getUserAccessToken();
        if (!userAccessToken) {
          console.error("Failed to obtain user access token");
          return;
        }
        console.log(userAccessToken);

        const response = await axios.post(
          "http://127.0.0.1:8000/passwortverwalten/",
          newUser,
          {
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${userAccessToken}`,
            },
          }
        );

        if (response.status === 200) {
          //Passwort erfolgreich geändert
          console.log("Password successfully changed:", response.data);
          //Popup anzeigen
          showSuccessPopup();
          setPassword(newPassword);
          console.log("old password:", password, " new password", newPassword);
          /*showSuccessPopup();*/
        }
      } catch (error) {
        //Fehlerbehandlung
        console.error("Error changing password:", error.message);
        if (error.response) {
          console.error("Server response data:", error.response.data);
          //Fehlermeldung anzeigen oder Fehler wie erforderlich behandeln
        }
      }
    }
  };

  return (
    <div className={styles.wrapper}>
      {/* Popup anzeigen, wenn showSuccessPopup wahr ist */}
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
          <div className="input-container">
            <input
              type="password"
              placeholder="Altes Passwort"
              value={oldPassword}
              onChange={(e) => {
                setOldPassword(e.target.value);
                checkFormValidity(
                  e.target.value,
                  newPassword,
                  confirmNewPassword
                );
              }}
            />
            <input
              type="password"
              placeholder="Neues Passwort"
              value={newPassword}
              onChange={(e) => {
                setNewPassword(e.target.value);
                checkFormValidity(
                  oldPassword,
                  e.target.value,
                  confirmNewPassword
                );
              }}
            />
            <input
              type="password"
              placeholder="Neues Passwort bestätigen"
              value={confirmNewPassword}
              onChange={(e) => {
                setConfirmNewPassword(e.target.value);
                checkFormValidity(oldPassword, newPassword, e.target.value);
              }}
            />
            <button
              className={styles.changePasswordBtn}
              // Neue Klasse hier hinzufügen
              type="submit"
              disabled={!isFormValid}
            >
              Passwort ändern
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Profileseite;
