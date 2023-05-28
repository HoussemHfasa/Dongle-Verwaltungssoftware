import React, { useState } from "react";
import "./DongleAnfordern.css";
import NavbarWrapper from "../Components/NavbarWrapper"; // Import NavbarWrapper

const DongleAnfordern = () => {
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

  return (
    <div className="DongleAnfordern-container">
      <NavbarWrapper />
      <div className="DongleAnfordern-header">
        <h1>Dongle Anfordern</h1>
      </div>

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
