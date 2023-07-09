import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import NavbarWrapper from "../Components/NavbarWrapper";
import styles from "./Adminseite.module.css";
import CustomuserTable from "./CustomuserTable";
import useAdminAccess from "./useAdminAccess";

const Adminseite = () => {
  const navigate = useNavigate();
  const { isAdmin, isLoading } = useAdminAccess();

  // Überprüft, ob der Benutzer ein Administrator ist und leitet ihn gegebenenfalls zur Übersichtseite weiter
  useEffect(() => {
    if (!isLoading && !isAdmin) {
      console.log("isAdmin:", isAdmin);
      navigate("/Übersichtseite");
    }
  }, [isAdmin, navigate, isLoading]);

  return (
    <div className={styles.container}>
      {/* Rahmen für Navbar und Hintergrund */}
      <div className={styles.frame7}>
        {/* Navbar */}
        <NavbarWrapper />
        {/* Rechteckiger Hintergrund */}
        <div className={styles.rectanglebackground}></div>
      </div>
      {/* Kontoerstellen-Button */}
      <button
        className={styles["Kontoerstellen"]}
        onClick={() => navigate("/Kontoerstellen")}
      >
        <span className={styles["Kontoerstellentext"]}>
          <span>Konto erstellen</span>
        </span>
      </button>
      {/* Benutzerdefinierte Tabelle */}
      <div className={`${styles["CustomuserTable"]} ${styles.tableContainer}`}>
        <CustomuserTable />
      </div>
    </div>
  );
};

export default Adminseite;
