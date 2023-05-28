import React, { forwardRef, useState } from "react";
import styles from "./Navbar.module.css";
import { useNavigate } from "react-router-dom"; // Change this import
import { useAuth } from "./AuthContext";

const ProfileMenu = forwardRef((props, ref) => {
  const [profileExploding, setProfileExploding] = useState(false);
  const [abmeldenExploding, setAbmeldenExploding] = useState(false);
  const navigate = useNavigate(); // Change this line
  const { setEmail, setPassword, setRole } = useAuth(); // Get setUsername from the context

  const handleProfileClick = () => {
    setProfileExploding(true);
    setTimeout(() => setProfileExploding(false), 500);
  };

  const handleAbmeldenClick = () => {
    setAbmeldenExploding(true);
    setTimeout(() => setAbmeldenExploding(false), 500);
    setEmail(null);
    setPassword(null);
    setRole(null);

    localStorage.removeItem("role"); // Remove the role from localStorage
    console.log("Role after removal:", localStorage.getItem("role"));

    navigate("/");
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
