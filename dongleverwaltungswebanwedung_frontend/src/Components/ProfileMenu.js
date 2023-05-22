import React, { forwardRef, useState } from "react";
import styles from "./NavbarKunde.module.css";

const ProfileMenu = forwardRef((props, ref) => {
  const [profileExploding, setProfileExploding] = useState(false);
  const [abmeldenExploding, setAbmeldenExploding] = useState(false);

  const handleProfileClick = () => {
    setProfileExploding(true);
    setTimeout(() => setProfileExploding(false), 500);
  };

  const handleAbmeldenClick = () => {
    setAbmeldenExploding(true);
    setTimeout(() => setAbmeldenExploding(false), 500);
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
