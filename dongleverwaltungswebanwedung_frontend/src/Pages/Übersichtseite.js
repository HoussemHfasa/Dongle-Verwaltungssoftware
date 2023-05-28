import React from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Übersichtseite.module.css";
import NavbarWrapper from "../Components/NavbarWrapper";
import DongleTable from "./DongleTable";

const Übersichtseite = () => {
  const navigate = useNavigate();

  return (
    <div className={styles.container}>
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
        <div className={styles["DongleTable"]}>
          <DongleTable />
        </div>

        {/* Dongle-Anforderungsbutton */}
        <button
          className={styles["Dongleanfordern"]}
          onClick={() => navigate("/DongleAnfordern")}
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
