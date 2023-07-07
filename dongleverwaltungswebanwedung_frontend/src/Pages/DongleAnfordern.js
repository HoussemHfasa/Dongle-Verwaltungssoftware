import axios from "axios";
import React, { useState } from "react";
import "./DongleAnfordern.css";
import NavbarWrapper from "../Components/NavbarWrapper";
import "react-datepicker/dist/react-datepicker.css";

const DongleAnfordern = () => {
  const [dongleId, setDongleId] = useState("");
  const [dongleName, setDongleName] = useState("");
  const [handler, setHandler] = useState("");
  const [standort, setStandort] = useState("");
  const [gueltigVon, setGueltigVon] = useState("");
  const [gueltigBis, setGueltigBis] = useState("");
  const [firmCode, setFirmCode] = useState("");
  const [projekt, setProjekt] = useState("");
  const [titel, setTitel] = useState("");
  const [beschreibung, setBeschreibung] = useState("");

  // Funktion zum Zurücksetzen des Formulars
  const resetForm = () => {
    setDongleId("");
    setDongleName("");
    setHandler("");
    setStandort("");
    setGueltigVon("");
    setGueltigBis("");
    setFirmCode("");
    setProjekt("");
    setTitel("");
    setBeschreibung("");
  };

  // Funktion zum Speichern der eingegebenen Daten
  const handleSave = async () => {
    try {

      const formattedGueltigVon = new Date(gueltigVon).toISOString().split("T")[0];
      const formattedGueltigBis = new Date(gueltigBis).toISOString().split("T")[0];

      const response = await axios.post(
        "http://localhost:8000/api/Dongleticket/create/",
         {
        dongle_seriennummer: dongleId,
        dongle_name: dongleName,
        gueltig_von: formattedGueltigVon,
        gueltig_bis: formattedGueltigBis,
        projekt: projekt,
        standort: standort,
        haendler: handler,
        firmcode: firmCode,
        titel: titel,
        beschreibung: beschreibung,
        erstellungsdatum: new Date().toISOString().split("T")[0],
        schliessungsdatum: new Date().toISOString().split("T")[0],
       
      });

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
    <div className="DongleAnfordern-container">
      {/* Navbar */}
      <NavbarWrapper />

      {/* Überschrift */}
      <div className="DongleAnfordern-header">
        <h1>Dongle anfordern</h1>
      </div>

      {/* Formular */}
      <div className="DongleAnfordern-form">
        {/* Dongle-ID (Seriennummer) */}
        <div className="form-row">
          <span className="form-label">Dongle-ID (Seriennummer)</span>
          <input
            type="text"
            placeholder="Dongle-ID (Seriennummer)"
            value={dongleId}
            onChange={(e) => setDongleId(e.target.value)}
          />
        </div>

        {/* Tittel */}
        <div className="form-row">
          <span className="form-label">Tittel</span>
          <input
            type="text"
            placeholder="Tittel"
            value={titel}
            onChange={(e) => setTitel(e.target.value)}
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

        {/* Dongle-Name */}
        <div className="form-row">
          <span className="form-label">Dongle-Name</span>
          <input
            type="text"
            placeholder="Dongle-Name"
            value={dongleName}
            onChange={(e) => setDongleName(e.target.value)}
          />
        </div>

        {/* Händler */}
        <div className="form-row">
          <span className="form-label">Händler</span>
          <input
            type="text"
            placeholder="Händler"
            value={handler}
            onChange={(e) => setHandler(e.target.value)}
          />
        </div>

        {/* Standort */}
        <div className="form-row">
          <span className="form-label">Standort</span>
          <input
            type="text"
            placeholder="Standort"
            value={standort}
            onChange={(e) => setStandort(e.target.value)}
          />
        </div>

        {/* Gültig von */}
        <div className="form-row">
          <span className="form-label">Gültig von</span>
          <input
            type="date"
            placeholder="yyyy-mm-dd"
            value={gueltigVon}
            onChange={(e) => setGueltigVon(e.target.value)}
          />
        </div>

        {/* Gültig bis */}
        <div className="form-row">
          <span className="form-label">Gültig bis</span>
          <input
            type="date"
            placeholder="yyyy-mm-dd"
            value={gueltigBis}
            onChange={(e) => setGueltigBis(e.target.value)}
          />
        </div>

        {/* FirmCode */}
        <div className="form-row">
          <span className="form-label">FirmCode</span>
          <input
            type="text"
            placeholder="FirmCode"
            value={firmCode}
            onChange={(e) => setFirmCode(e.target.value)}
          />
        </div>

        {/* Projekt */}
        <div className="form-row">
          <span className="form-label">Projekt</span>
          <input
            type="text"
            placeholder="Projekt"
            value={projekt}
            onChange={(e) => setProjekt(e.target.value)}
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

export default DongleAnfordern;
