import React, { forwardRef, useState } from "react";
import styles from "./Navbar.module.css";
import { useNavigate } from "react-router-dom"; // Change this import

const ProfileMenu = forwardRef((props, ref) => {
  const [profileExploding, setProfileExploding] = useState(false);
  const [abmeldenExploding, setAbmeldenExploding] = useState(false);
  const navigate = useNavigate(); // Change this line

  const handleProfileClick = () => {
    setProfileExploding(true);
    setTimeout(() => setProfileExploding(false), 500);
  };

  const handleAbmeldenClick = () => {
    setAbmeldenExploding(true);
    setTimeout(() => setAbmeldenExploding(false), 500);
    navigate("/"); // Change this line
  };

  return (
    <div className={styles["container1"]} ref={ref}>
      <button
        className={`${styles["profileButton"]} ${
          profileExploding ? styles["exploding"] : ""
        }`}
        onClick={handleProfileClick}
      >
        Profile
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
