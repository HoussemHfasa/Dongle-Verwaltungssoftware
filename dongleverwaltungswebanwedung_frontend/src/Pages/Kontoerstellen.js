import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import NavbarWrapper from "../Components/NavbarWrapper";
import styles from "./Kontoerstellen.module.css";

const Kontoerstellen = () => {
  const navigate = useNavigate();
  const [role1, setRole1] = useState("");
  const [email1, setEmail1] = useState("");
  const [confirmEmail, setConfirmEmail] = useState("");
  const [name1, setName1] = useState("");
  const [password1, setPassword1] = useState("");
  const [firmCode, setFirmCode] = useState("");

  const isEmailValid = (emailAddress) => {
    const emailRegex = /^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/;
    return emailRegex.test(emailAddress);
  };

  const isFormValid =
    role1 &&
    isEmailValid(email1) &&
    email1 === confirmEmail &&
    name1 &&
    password1 &&
    (role1 !== "Kunde" || firmCode);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (isFormValid) {
      const newUser = {
        email: email1,
        name: name1,
        role: role1,
        password: password1,
        firm_code: firmCode,
      };
      console.log({ role1, email1, name1, password1, firmCode });
      try {
        const adminAccessToken = response.data.access; // Replace this with the actual admin access token
        console.log(adminAccessToken);

        const response = await axios.post(
          "http://127.0.0.1:8000/users/",
          newUser,
          {
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${adminAccessToken}`,
            },
          }
        );

        if (response.status === 201) {
          console.log("New user created:", response.data);
          // Show a success message or redirect to another page
          navigate("/some-success-page");
        }
      } catch (error) {
        console.error("Error creating user:", error.message);
        if (error.response) {
          console.error("Server response data:", error.response.data);
          // Show an error message or handle the error as needed
        }
      }
    }
  };

  return (
    <div className={styles.wrapper}>
      <div className={styles.container}>
        {/* Rahmen für Navbar und Hintergrund */}
        <div className={styles.frame7}>
          {/* Navbar */}
          <NavbarWrapper />
          {/* Rechteckiger Hintergrund */}
          <div className={styles.rectanglebackground}></div>
        </div>
        <form onSubmit={handleSubmit}>
          <select value={role1} onChange={(e) => setRole1(e.target.value)}>
            <option value="">Rolle wählen</option>
            <option value="Admin">Admin</option>
            <option value="Verwalter">Verwalter</option>
            <option value="Kunde">Kunde</option>
          </select>
          <input
            type="email"
            placeholder="E-Mail"
            value={email1}
            onChange={(e) => setEmail1(e.target.value)}
          />
          <input
            type="email"
            placeholder="E-Mail bestätigen"
            value={confirmEmail}
            onChange={(e) => setConfirmEmail(e.target.value)}
          />
          <input
            type="text"
            placeholder="Name"
            value={name1}
            onChange={(e) => setName1(e.target.value)}
          />
          <input
            type="password"
            placeholder="Passwort"
            value={password1}
            onChange={(e) => setPassword1(e.target.value)}
          />
          {role1 === "Kunde" && (
            <input
              type="text"
              placeholder="Firmencode"
              value={firmCode}
              onChange={(e) => setFirmCode(e.target.value)}
            />
          )}
          <button type="submit" disabled={!isFormValid}>
            Benutzer erstellen
          </button>
        </form>
      </div>
    </div>
  );
};

export default Kontoerstellen;
