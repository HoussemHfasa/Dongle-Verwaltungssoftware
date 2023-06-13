import React, { useState, useRef, useEffect } from "react";
import styles from "./Navbar.module.css";
import user_image from "./user.png";
import Notification_image from "./active.png";
import NotificationMenu from "./NotificationMenu";
import ProfileMenu from "./ProfileMenu";
import gfaiLogo from "./gfai_logo.png";
import { useNavigate } from "react-router-dom";

const NavbarAdmin = (props) => {
  // State für die Anzeige der Popup-Menüs
  const [showProfilePopup, setShowProfilePopup] = useState(false);
  const [showNotificationPopup, setShowNotificationPopup] = useState(false);

  // Referenzen zum Erkennen von Klicks außerhalb der Popup-Menüs
  const profileMenuRef = useRef(null);
  const notificationMenuRef = useRef(null);
  const profileButtonRef = useRef(null);
  const notificationButtonRef = useRef(null);

  // Funktion zum Umschalten der Anzeige des Profil-Popup-Menüs
  const toggleProfilePopup = () => {
    setShowProfilePopup(!showProfilePopup);
  };

  // Funktion zum Umschalten der Anzeige des Benachrichtigungs-Popup-Menüs
  const toggleNotificationPopup = () => {
    setShowNotificationPopup(!showNotificationPopup);
  };

  // Hook zum Navigieren innerhalb der Anwendung
  const navigate = useNavigate();

  // Funktion zum Behandeln von Klicks außerhalb der Popup-Menüs
  const handleClickOutside = (e) => {
    if (
      showProfilePopup &&
      profileMenuRef.current &&
      !profileMenuRef.current.contains(e.target) &&
      !profileButtonRef.current.contains(e.target)
    ) {
      toggleProfilePopup();
    }

    if (
      showNotificationPopup &&
      notificationMenuRef.current &&
      !notificationMenuRef.current.contains(e.target) &&
      !notificationButtonRef.current.contains(e.target)
    ) {
      toggleNotificationPopup();
    }
  };

  // Hinzufügen eines EventListeners, um Klicks außerhalb der Popup-Menüs zu erkennen
  useEffect(() => {
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [showProfilePopup, showNotificationPopup, handleClickOutside]); // Füge handleClickOutside zur Abhängigkeiten-Liste hinzu

  return (
    <div className={styles["container"]}>
      <div className={styles["frame"]}>
        {showProfilePopup && <ProfileMenu ref={profileMenuRef} />}
        {showNotificationPopup && (
          <NotificationMenu ref={notificationMenuRef} />
        )}
        <div className={styles["rectanglebackground"]}></div>
        <img alt="GFAI Logo" src={gfaiLogo} className={styles["logo"]} />
        <button
          className={styles["home"]}
          onClick={() => navigate("/Übersichtseite")}
        >
          Übersichtsseite
        </button>
        <button
          className={styles["lizenz"]}
          onClick={() => navigate("/Lizenübersicht")}
        >
          Lizenzübersicht
        </button>
        <button className={styles["anfrage"]}>Anfrage</button>
        <button className={styles["admin"]} onClick={() => navigate("/Admin")}>
          Admin
        </button>
        <button
          className={styles["profileImageButton"]}
          onClick={toggleProfilePopup}
          ref={profileButtonRef}
        >
          <img
            alt="user_image"
            src={user_image}
            className={styles["profileimage"]}
          />
        </button>
        <button
          className={styles["notificationImageButton"]}
          onClick={toggleNotificationPopup}
          ref={notificationButtonRef}
        >
          <img
            alt="Notification_image"
            src={Notification_image}
            className={styles["notificationimage"]}
          />
        </button>
      </div>
    </div>
  );
};

export default NavbarAdmin;
