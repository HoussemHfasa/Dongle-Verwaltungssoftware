import React from "react";
import { useNavigate, useLocation } from "react-router-dom";
import styles from "./Übersichtseite.module.css";
import NavbarAdmin from "../Components/NavbarAdmin";
import NavbarKunde from "../Components/NavbarKunde";
import NavbarVerwalter from "../Components/NavbarVerwalter";

const Übersichtseite = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const username = location.state?.username;

  const renderNavbar = () => {
    if (username === "admin" || username === "Admin") {
      return <NavbarAdmin />;
    } else if (username === "verwalter" || username === "Verwalter") {
      return <NavbarVerwalter />;
    } else if (username === "kunde" || username === "Kunde") {
      return <NavbarKunde />;
    } else {
      return <></>;
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.frame7}>
        <div className={styles.rectanglebackground}></div>
        {renderNavbar()}
      </div>
      <div className={styles.content}>
        übersichtseite
        <button
          className={styles["Dongleanfordern"]}
          onClick={() => navigate("/DongleAnfordern", { state: { username } })}
        >
          <span className={styles["Dongleanforderntext"]}>
            <span>Dongle anfordern</span>
          </span>
        </button>
      </div>
    </div>
  );
};
export default Übersichtseite;
