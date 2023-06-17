import React, { useState } from "react";
import "./Donglehinzufuegen.css";
import NavbarWrapper from "../Components/NavbarWrapper";
import axios from "axios";
import "react-datepicker/dist/react-datepicker.css";

const Donglehinzufuegen = () => {
  const [dongleId, setDongleId] = useState("");
  const [productName, setProductName] = useState("");
  const [handler, setHandler] = useState("");
  const [standort, setStandort] = useState("");
  const [gültigVon, setGültigVon] = useState("");
  const [gültigBis, setGültigBis] = useState("");
  const [firmCode, setFirmCode] = useState("");
  const [projekt, setProjekt] = useState("");

  // Funktion zum Zurücksetzen des Formulars
  const resetForm = () => {
    setDongleId("");
    setProductName("");
    setHandler("");
    setStandort("");
    setGültigVon("");
    setGültigBis("");
    setFirmCode("");
    setProjekt("");
  };

  // Funktion zum Speichern der eingegebenen Daten
  const handleSave = async () => {
    try {
      const formattedGültigVon = new Date(gültigVon)
        .toISOString()
        .split("T")[0];
      const formattedGültigBis = new Date(gültigBis)
        .toISOString()
        .split("T")[0];

      const response = await axios.post(
        "http://localhost:8000/api/dongle/create/",
        {
          serien_nr: dongleId,
          name: productName,
          gueltig_von: formattedGültigVon,
          gueltig_bis: formattedGültigBis,
          projekt_produkt: projekt,
          standort: standort,
          haendler: handler,
          datum_letzte_aenderung: new Date().toISOString().split("T")[0],
          datum_erstausgabe: new Date().toISOString().split("T")[0],
          firmcode: firmCode,
        }
      );

      if (response.status === 201) {
        alert("Dongle erfolgreich gespeichert!");
        resetForm();
      } else {
        alert("Fehler beim Speichern des Dongles");
      }
    } catch (error) {
      console.error("Fehler beim Speichern des Dongles:", error);

      if (error.response && error.response.data) {
        const errorMessage = error.response.data;
        alert("Fehler beim Speichern des Dongles: " + errorMessage);
      } else {
        alert("Fehler beim Speichern des Dongles: " + error.message);
      }
    }
  };

  return (
    <div className="DongleAnfordern-container">
      {/* Navbar */}
      <NavbarWrapper />

      {/* Überschrift */}
      <div className="DongleAnfordern-header">
        <h1>Dongle hinzufügen</h1>
      </div>

      {/* Formular */}
      <div className="DongleAnfordern-form">
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
        {/* Produktname */}
        <div className="form-row">
          <span className="form-label">Produktname</span>
          <input
            type="text"
            placeholder="Produktname"
            value={productName}
            onChange={(e) => setProductName(e.target.value)}
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
            value={gültigVon}
            onChange={(e) => setGültigVon(e.target.value)}
          />
        </div>
        {/* Gültig bis */}
        <div className="form-row">
          <span className="form-label">Gültig bis</span>
          <input
            type="date"
            placeholder="yyyy-mm-dd"
            value={gültigBis}
            onChange={(e) => setGültigBis(e.target.value)}
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
        {/* Datum erste Ausgabe */}

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

export default Donglehinzufuegen;
