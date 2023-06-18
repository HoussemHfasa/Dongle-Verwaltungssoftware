// Importiere notwendige Pakete und Komponenten
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Passwortzurücksetzung.module.css";
import axios from "axios";
import { AiOutlineReload } from "react-icons/ai";

// Passwortzurücksetzung-Komponente
const Passwortzurücksetzung = () => {
  // Verwende den 'useNavigate' Hook, um die Navigation zu ermöglichen
  const navigate = useNavigate();

  // Verwalte den Zustand für E-Mail, Bestätigungs-E-Mail, Captcha-Eingabe und zufälliges Captcha
  const [inputEmail, setInputEmail] = useState("");
  const [confirmEmail, setConfirmEmail] = useState("");
  const [captchaInput, setCaptchaInput] = useState("");
  const [captcha, setCaptcha] = useState(generateRandomCaptcha());
  const [showPopup, setShowPopup] = useState(false);

  // Funktion zum Generieren eines zufälligen Captchas
  function generateRandomCaptcha() {
    return Math.random().toString(36).substring(2, 8).toUpperCase();
  }

  // Funktion zum Aktualisieren des Captchas
  function refreshCaptcha() {
    setCaptcha(generateRandomCaptcha());
  }

  // Überprüfe, ob das Formular gültig ist
  const isFormValid =
    inputEmail.length > 0 &&
    confirmEmail.length > 0 &&
    captchaInput.length > 0 &&
    inputEmail === confirmEmail &&
    captcha === captchaInput;

  // Funktion zum Anzeigen des Erfolgspopups
  const showSuccessPopup = () => {
    console.log("showSuccessPopup called");
    setShowPopup(true);
  };

  // Erfolgspopup-Komponente
  const SuccessPopup = () => (
    <div className={styles.popupWrapper}>
      <div className={styles.popup}>
        <p>Passwort zurückgesetzt</p>
        <button className={styles.okButton} onClick={() => navigate("/")}>
          OK
        </button>
      </div>
    </div>
  );

  // Funktion zum Senden der Passwortzurücksetzung
  const handlePasswordResetSubmit = async (e) => {
    e.preventDefault();
    if (isFormValid) {
      const newUser = {
        email: inputEmail,
      };
      console.log({ inputEmail });
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/Passwortzuruecksetzung/",
          newUser
        );

        if (response.status === 200) {
          showSuccessPopup();
        }
      } catch (error) {
        console.error("Error sending password:", error.message);
        if (error.response) {
          console.error("Server response data:", error.response.data);
          // Show an error message or handle the error as needed
        }
      }
    }
  };

  // Rendere die Passwortzurücksetzung-Komponente
  return (
    <div className={styles.container}>
      {showPopup && <SuccessPopup />}
      <div className={styles.Background}>
        <div className={styles["white-rectangle"]} />
        <form onSubmit={handlePasswordResetSubmit}>
          {/* E-Mail-Feld */}
          <input
            type="text"
            placeholder="Schreiben Sie Ihr E-Mail"
            className={styles.textbox_Email}
            onChange={(e) => setInputEmail(e.target.value)}
          />
          <div className={styles["frame-Email"]}>E-Mail</div>

          {/* Bestätigen Sie das E-Mail-Feld */}
          <input
            type="text"
            placeholder="Bestätigen Sie Ihr E-Mail"
            className={styles.textbox_ConfirmEmail}
            onChange={(e) => setConfirmEmail(e.target.value)}
          />
          <div className={styles["frame-ConfirmEmail"]}>E-Mail bestätigen</div>

          {/* Captcha */}
          <div className={styles["frame-Captcha-container"]}>
            <div className={styles["frame-Captcha"]}>{captcha}</div>
            <AiOutlineReload
              className={styles["refresh-captcha"]}
              onClick={refreshCaptcha}
            />
          </div>
          <input
            type="text"
            placeholder="Geben Sie das Captcha ein"
            className={styles.textbox_CaptchaInput}
            onChange={(e) => setCaptchaInput(e.target.value)}
          />

          {/* Passwort-zurücksetzen-Knopf */}
          <button
            className={styles["rectangular-button"]}
            type="submit"
            disabled={!isFormValid}
          >
            Passwort zurücksetzen
          </button>
        </form>
      </div>
    </div>
  );
};

// Exportiere die Passwortzurücksetzung-Komponente
export default Passwortzurücksetzung;
