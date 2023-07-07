import React from "react";
import NavbarWrapper from "../Components/NavbarWrapper";
import styles from "./Adminseite.module.css";

import TicketTable from "./TicketTable";

const Lizenzanfordernantwort = () => {
  return (
    <div className={styles.container}>
      {/* Rahmen für Navbar und Hintergrund */}
      <div className={styles.frame7}>
        {/* Navbar */}
        <NavbarWrapper />
        {/* Rechteckiger Hintergrund */}
        <div className={styles.rectanglebackground}></div>
      </div>

      <div className={`${styles["CustomuserTable"]} ${styles.tableContainer}`}>
        <TicketTable />
      </div>
    </div>
  );
};

export default Lizenzanfordernantwort;
