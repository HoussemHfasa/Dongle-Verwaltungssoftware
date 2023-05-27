import React from "react";
import { useNavigate, useLocation } from "react-router-dom";
import styles from "./Übersichtseite.module.css";
import NavbarWrapper from "../Components/NavbarWrapper"; // Import NavbarWrapper

import LizenzTable from "./LizenzTable";


const Lizensüberscht = () => {
  const navigate = useNavigate();
  return (
    <div className={styles.container}>
      <div className={styles.frame7}>
        <NavbarWrapper />
        <div className={styles.rectanglebackground}></div>
      </div>
      
      <div className={styles.content}>
        
        <LizenzTable/>
        
      </div>
    </div>
  );
};
export default Lizensüberscht;
