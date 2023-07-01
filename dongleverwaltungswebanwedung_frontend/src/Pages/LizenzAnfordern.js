import React, { useState } from "react";
import "./LizenzAnfordern.css";
import NavbarWrapper from "../Components/NavbarWrapper";
import axios from "axios";
import "react-datepicker/dist/react-datepicker.css";


const Lizenzanfordern = () => {
  const [dongleId, setDongleId] = useState("");
  const [lizenzname, setLizenzname] = useState("");
  const [tittel, setTittel] = useState("");
  const [beschreibung, setBeschreibung] = useState("");

  // Funktion zum Zurücksetzen des Formulars
  const resetForm = () => {
    setDongleId("");
    setLizenzname("");
    setTittel("");
    setBeschreibung("");
  };

  // Funktion zum Speichern der eingegebenen Daten
  const handleSave = async () => {
    try {
      const response = await axios.post(
        "http://localhost:8000/api/ticket/create/",
        {
          dongle_seriennummer: dongleId,
          titel: tittel,
          beschreibung: beschreibung,
          lizenzname: lizenzname,
          erstellungsdatum: new Date().toISOString().split("T")[0],
          schliessungsdatum: new Date().toISOString().split("T")[0],
          status: "offen",
        }
      );
  
      if (response.status === 201) {
        alert("Ihre Anfrage wurde gesendet!");
        resetForm();
      } else {
        alert("Fehler beim Senden der Anfrage.");
      }
    } catch (error) {
      console.error("Fehler beim Senden der Anfrage", error);
  
      if (error.response && error.response.data) {
        const errorMessage = error.response.data;
        alert("Fehler beim Senden der Anfrage: " + errorMessage);
      } else {
        alert("Fehler beim Senden der Anfrage: " + error.message);
      }
    }
  };
  

  return (
    <div className="LizenzAnfordern-container">
      {/* Navbar */}
      <NavbarWrapper />

      {/* Überschrift */}
      <div className="LizenzAnfordern-header">
        <h1>Lizenz anfordern</h1>
      </div>

      {/* Formular */}
      <div className="LizenzAnfordern-form">
        {/* Dongle-ID (Seriennummer) */}
        <div className="form-row">
          <span className="form-label">Dongle-ID(Seriennummer)</span>
          <input
              type="text"
              placeholder="Dongle-ID (Seriennummer)"
              value={dongleId}
            onChange={(e) => setDongleId(e.target.value)}
          />
        </div>
       
        {/* Lizenzname */}
        <div className="form-row">
          <span className="form-label">Lizenzname</span>
          <input
            type="text"
            placeholder="Lizenzname"
            value={lizenzname}
            onChange={(e) => setLizenzname(e.target.value)}
          />
        </div>
        {/* tittel */}
        <div className="form-row">
          <span className="form-label">Tittel</span>
          <input
            type="text"
            placeholder="Tittel"
            value={tittel}
            onChange={(e) => setTittel(e.target.value)}
          />
        </div>
        {/* Beschreibung */}
        <div className="form-row">
          <span className="form-label">Beschreibung</span>
          <input
            type="text"
            placeholder="Beschreibung"
            value={beschreibung}
            onChange={(e) => setBeschreibung(e.target.value)}
          />
        </div>
        {/* Button-Container */}
        <div className="button-container">
          {/* Stornieren-Button */}
          <button className="cancel-button" onClick={() => resetForm()}>
            Stornieren
          </button>
          {/* Speichern-Button */}
          <button className="save-button" onClick={() => handleSave()}>
            Speichern
          </button>
        </div>
      </div>
    </div>
  );
};

export default Lizenzanfordern;
