import React from "react";
import NavbarWrapper from "../Components/NavbarWrapper";
import styles from "./Übersichtseite.module.css";
import LizenzTable from "./LizenzTable";
import { useAuth } from "../Components/AuthContext"; // Import useAuth
import { useNavigate } from "react-router-dom"; // Import useNavigate

const Lizenzübersicht = () => {
  const { role } = useAuth(); // Get the role from the AuthContext
  const navigate = useNavigate(); // Hook for navigation

  return (
    <div className={styles.container}>
      <div className={styles.frame7}>
        <NavbarWrapper />
        <div className={styles.rectanglebackground}></div>
      </div>

      <div className={styles.content}>
        <div
          className={`${styles["Lizenz"]} ${styles.tableContainer} ${styles.tableScrollable}`}
        >
          <LizenzTable />
        </div>

        {role === "Admin" || role === "Verwalter" ? (
          <button
            className={styles["Donglehinzufuegen"]}
            onClick={() => navigate("/Lizenzhinzufuegen")}
          >
            <span className={styles["Donglehinzufuegentext"]}>
              <span>Lizenz hinzufügen</span>
            </span>
          </button>
        ) : (
          role === "Kunde" && (
            <button
              className={styles["Donglehinzufuegen"]}
              onClick={() => navigate("/Profileseite")}
            >
              <span className={styles["Donglehinzufuegentext"]}>
                <span>Lizenz anfordern</span>
              </span>
            </button>
          )
        )}
      </div>
    </div>
  );
};

export default Lizenzübersicht;
