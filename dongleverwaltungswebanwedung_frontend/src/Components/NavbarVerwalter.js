import React from "react";
import styles from "./NavbarKunde.module.css";
import user_image from "./user.png";
import Notification_image from "./active.png";

const NavbarVerwalter = (props) => {
  return (
    <div className={styles["container"]}>
      <div className={styles["frame"]}>
        <img
          alt="Rectangle352356"
          src="/playground_assets/rectangle352356-32rk-200h.png"
          className={styles["rectanglebackground"]}
        />
        <span className={styles["logo"]}>
          <span>Logo</span>
        </span>
        <button className={styles["home"]}>Übersichtsseite</button>
        <button className={styles["lizenz"]}>Lizensübersicht</button>
        <button className={styles["anfrage"]}>Anfrage</button>
        <button className={styles["profileImageButton"]}>
          <img
            alt="user_image"
            src={user_image}
            className={styles["profileimage"]}
          />
        </button>

        <button className={styles["notificationImageButton"]}>
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
