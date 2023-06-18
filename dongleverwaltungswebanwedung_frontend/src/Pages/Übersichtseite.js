import React from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Übersichtseite.module.css";
import NavbarWrapper from "../Components/NavbarWrapper";
import DongleTable from "./DongleTable";
import { useAuth } from "../Components/AuthContext";

const Übersichtseite = () => {
  const navigate = useNavigate();
  const { role } = useAuth();

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
        <div className={`${styles["DongleTable"]} ${styles.tableContainer}`}>
          {/* Neue CSS-Klasse hier hinzufügen */}
          <DongleTable />
        </div>

        {/* Dongle-Anforderungsbutton */}
        {role === "Admin" ||
        role ===
          "Verwalter" /*Dongle-Hinzufügeknopf anzeigen wenn Benutzer Admin oder Verwalter ist*/ ? (
          <button
            className={styles["Donglehinzufuegen"]}
            onClick={() => navigate("/Donglehinzufuegen")}
          >
            <span className={styles["Donglehinzufuegentext"]}>
              <span>Dongle hinzufügen</span>
            </span>
          </button>
        ) : (
          role ===
            "Kunde" /*Dongleanforderungsknopf anzeigen, wenn Benutzer Kunde ist */ && (
            <button
              className={styles["Donglehinzufuegen"]}
              onClick={() => navigate("/Lizenübersicht")}
            >
              <span className={styles["Donglehinzufuegentext"]}>
                <span>Dongle anfordern</span>
              </span>
            </button>
          )
        )}
      </div>
    </div>
  );
};

export default Übersichtseite;
