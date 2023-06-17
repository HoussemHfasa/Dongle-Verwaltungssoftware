import React, { forwardRef, useState } from "react";
import styles from "./Navbar.module.css";
import { useNavigate } from "react-router-dom";
import { useAuth } from "./AuthContext";

const ProfileMenu = forwardRef((props, ref) => {
  const [profileExploding /*setProfileExploding*/] = useState(false);
  const [abmeldenExploding, setAbmeldenExploding] = useState(false);
  const navigate = useNavigate();
  const { setEmail, setPassword, setRole } = useAuth();

  /*// Funktion zum Behandeln des Klicks auf den Profil-Button
  const handleProfileClick = () => {
    setProfileExploding(true);
    setTimeout(() => setProfileExploding(false), 500);
  };*/

  // Funktion zum Behandeln des Klicks auf den Abmelden-Button
  const handleAbmeldenClick = () => {
    setAbmeldenExploding(true);
    setTimeout(() => setAbmeldenExploding(false), 500);
    setEmail(null);
    setPassword(null);
    setRole(null);

    // Entfernen der Rolle aus dem localStorage
    localStorage.removeItem("role");
    localStorage.removeItem("email");
    localStorage.removeItem("password");
    console.log("Rolle nach Entfernung:", localStorage.getItem("role"));

    // Navigieren zum Startbildschirm
    navigate("/");
  };

  return (
    // Verwenden von forwardRef, um die ref-Instanz von außerhalb der Komponente zu verwalten
    <div className={styles["container1"]} ref={ref}>
      <button
        className={`${styles["profileButton"]} ${
          profileExploding ? styles["exploding"] : ""
        }`}
        onClick={() => navigate("/Profileseite")}
      >
        Profil
      </button>
      <button
        className={`${styles["abmeldenButton"]} ${
          abmeldenExploding ? styles["exploding"] : ""
        }`}
        onClick={handleAbmeldenClick}
      >
        Abmelden
      </button>
    </div>
  );
});

export default ProfileMenu;
