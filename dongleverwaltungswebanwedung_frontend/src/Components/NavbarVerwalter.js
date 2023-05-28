import React, { useState, useRef, useEffect } from "react";
import styles from "./Navbar.module.css";
import user_image from "./user.png";
import Notification_image from "./active.png";
import NotificationMenu from "./NotificationMenu";
import ProfileMenu from "./ProfileMenu";
import gfaiLogo from "./gfai_logo.png";
import { useNavigate } from "react-router-dom";

const NavbarVerwalter = (props) => {
  const [showProfilePopup, setShowProfilePopup] = useState(false);
  const [showNotificationPopup, setShowNotificationPopup] = useState(false);
  const profileMenuRef = useRef(null);
  const notificationMenuRef = useRef(null);
  const profileButtonRef = useRef(null);
  const notificationButtonRef = useRef(null);

  const toggleProfilePopup = () => {
    setShowProfilePopup(!showProfilePopup);
  };
  const navigate = useNavigate();

  const toggleNotificationPopup = () => {
    setShowNotificationPopup(!showNotificationPopup);
  };

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

  useEffect(() => {
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [showProfilePopup, showNotificationPopup]);

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
          onClick={() => navigate("/Übersichtseite")} // Add the navigate function here
        >
          Übersichtsseite
        </button>
        <button className={styles["lizenz"]}>Lizensübersicht</button>
        <button className={styles["anfrage"]}>Anfrage</button>
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
        <a
          href="https://www.flaticon.com/free-icons/notification"
          title="notification icons"
        >
          Notification icons created by Pixel perfect - Flaticon
        </a>
      </div>
    </div>
  );
};
export default NavbarVerwalter;
