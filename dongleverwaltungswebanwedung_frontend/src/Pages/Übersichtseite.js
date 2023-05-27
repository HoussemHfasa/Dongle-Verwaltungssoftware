import React from "react";
import { useNavigate, useLocation } from "react-router-dom";
import styles from "./Übersichtseite.module.css";
import NavbarWrapper from "../Components/NavbarWrapper"; // Import NavbarWrapper
import DongleTable from './DongleTable';


const Übersichtseite = () => {
  const navigate = useNavigate();
  return (
    <div className={styles.container}>
      <div className={styles.frame7}>
        <NavbarWrapper />
        <div className={styles.rectanglebackground}></div>
      </div>
      
      <div className={styles.content}>
        übersichtseite
        <DongleTable/>
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
