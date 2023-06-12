import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import NavbarWrapper from "../Components/NavbarWrapper";
import styles from "./Adminseite.module.css";
import CustomuserTable from "./CustomuserTable";
import useAdminAccess from "./useAdminAccess";

const Adminseite = () => {
  const navigate = useNavigate();
  const { isAdmin, isLoading } = useAdminAccess();

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
      {/* Kontoerstellen-button */}
      <button
        className={styles["Kontoerstellen"]}
        onClick={() => navigate("/Kontoerstellen")}
      >
        <span className={styles["Kontoerstellentext"]}>
          <span>Kontoerstellen</span>
        </span>
      </button>
      <div className={styles["CustomuserTable"]}>
        <CustomuserTable />
      </div>
    </div>
  );
};

export default Adminseite;
