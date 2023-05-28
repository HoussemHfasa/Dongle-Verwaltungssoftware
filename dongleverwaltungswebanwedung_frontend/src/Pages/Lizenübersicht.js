import React from "react";
import { useNavigate, useLocation } from "react-router-dom";
import NavbarWrapper from "../Components/NavbarWrapper"; // Import NavbarWrapper
import styles from "./Übersichtseite.module.css";

import LizenzTable from "./LizenzTable";

const Lizenzübersicht = () => {
  const navigate = useNavigate();
  return (
    <div className={styles.container}>
      <div className={styles.frame7}>
        <NavbarWrapper />
        <div className={styles.rectanglebackground}></div>
      </div>

      
        <div className={styles.Lizenz}>
          <div className={styles["Lizenz"]}><LizenzTable /></div>
          
        </div>
      
    </div>
  );
};

export default Lizenzübersicht;