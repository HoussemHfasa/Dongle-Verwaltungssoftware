import React, { useState } from "react";
import { useLocation } from "react-router-dom";
import NavbarAdmin from "../Components/NavbarAdmin";
import NavbarKunde from "../Components/NavbarKunde";
import NavbarVerwalter from "../Components/NavbarVerwalter";
import "./DongleAnfordern.css";

const DongleAnfordern = () => {
  const location = useLocation();
  const username = location.state?.username;
  console.log("Username:", username);

  const [dongleId, setDongleId] = useState("");
  const [productName, setProductName] = useState("");
  const [email, setEmail] = useState("");
  const [handler, setHandler] = useState("");
  const [ablaufdatum, setAblaufdatum] = useState("");

  const resetForm = () => {
    setDongleId("");
    setProductName("");
    setEmail("");
    setHandler("");
    setAblaufdatum("");
  };

  const handleSave = async () => {
    // ...
  };

  const renderNavbar = () => {
    if (username === "admin" || username === "Admin") {
      return <NavbarAdmin />;
    } else if (username === "verwalter" || username === "Verwalter") {
      return <NavbarVerwalter />;
    } else if (username === "kunde" || username === "Kunde") {
      return <NavbarKunde />;
    } else {
      return <></>;
    }
  };

  return (
    <div className="DongleAnfordern-container">
      {renderNavbar()}
      <div className="DongleAnfordern-header">
        <h1>Dongle Anfordern</h1>
      </div>
      <h2 style={{ textAlign: "center", marginTop: "50px" }}>
        Username: {username}
      </h2>
      <div className="DongleAnfordern-form">
        <div className="form-row">
          <span className="form-label">Dongle-ID(Seriennummer)</span>
          <input
            type="text"
            placeholder=" "
            value={dongleId}
            onChange={(e) => setDongleId(e.target.value)}
          />
        </div>
        <div className="form-row">
          <span className="form-label">Produktname</span>
          <input
            type="text"
            placeholder=" "
            value={productName}
            onChange={(e) => setProductName(e.target.value)}
          />
        </div>
        <div className="form-row">
          <span className="form-label">email</span>
          <input
            type="text"
            placeholder=" "
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div className="form-row">
          <span className="form-label">Händler</span>
          <input
            type="text"
            placeholder=" "
            value={handler}
            onChange={(e) => setHandler(e.target.value)}
          />
        </div>
        <div className="form-row">
          <span className="form-label">Ablaufdatum</span>
          <input
            type="text"
            placeholder=" "
            value={ablaufdatum}
            onChange={(e) => setAblaufdatum(e.target.value)}
          />
        </div>
        <div className="button-container">
          <button className="cancel-button" onClick={() => resetForm()}>
            Stornieren
          </button>
          <button className="save-button" onClick={() => handleSave()}>
            Speichern
          </button>
        </div>
      </div>
    </div>
  );
};
export default DongleAnfordern;
