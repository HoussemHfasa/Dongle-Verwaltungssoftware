import React, { useState, useEffect } from "react";
import "./Lizenzhinzufügen.css";
import NavbarWrapper from "../Components/NavbarWrapper";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../Components/AuthContext";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

const Lizenzhinzufuegen = () => {
  const navigate = useNavigate();
  const [mitarbeiter, setMitarbeiter] = useState("");
  const [lizenzName, setLizenzName] = useState("");
  const [einheiten, setEinheiten] = useState("");
  const [productCode, setProductCode] = useState("");
  const [gültigVon, setGültigVon] = useState("");
  const [gültigBis, setGültigBis] = useState("");
  const [firmCode, setFirmCode] = useState("");
  const [projekt, setProjekt] = useState("");
  const [lizenzAnzahl, setLizenzAnzahl] = useState("");

  // Funktion zum Zurücksetzen des Formulars
  const resetForm = () => {
    setMitarbeiter("");
    setLizenzName("");
    setEinheiten("");
    setProductCode("");
    setGültigVon("");
    setGültigBis("");
    setFirmCode("");
    setProjekt("");
    setLizenzAnzahl("");
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
        "http://localhost:8000/api/license/create/",
        {
          lizenzanzahl: lizenzAnzahl,
          lizenzname: lizenzName,
          gueltig_von: formattedGültigVon,
          gueltig_bis: formattedGültigBis,
          projekt: projekt,
          einheiten: einheiten,
          productcode: productCode,
          mitarbeiter: mitarbeiter,
          firmcode: firmCode,
        }
      );

      if (response.status === 201) {
        alert("Lizenz erfolgreich gespeichert!");
        resetForm();
      } else {
        alert("Fehler beim Speichern des Lizenzes");
      }
    } catch (error) {
      console.error("Fehler beim Speichern des Lizenzes:", error);
      alert("Fehler beim Speichern des Lizenzes: " + error.message);
    }
  };

  return (
    <div className="Lizenzhinzufügen-container">
      {/* Navbar */}
      <NavbarWrapper />

      {/* Überschrift */}
      <div className="Lizenzhinzufügen-header">
        <h1>Lizenz hinzufügen</h1>
      </div>

      {/* Formular */}
      <div className="Lizenzhinzufügen-form">
        {/* Dongle-ID (Seriennummer) */}
        <div className="form-row">
          <span className="form-label">Mitarbeiter</span>
          <input
            type="text"
            placeholder="Mitarbeiter"
            value={mitarbeiter}
            onChange={(e) => setMitarbeiter(e.target.value)}
          />
        </div>
        {/* Produktname */}
        <div className="form-row">
          <span className="form-label">LizenzName</span>
          <input
            type="text"
            placeholder="lizenzname"
            value={lizenzName}
            onChange={(e) => setLizenzName(e.target.value)}
          />
        </div>
        {/* Händler */}
        <div className="form-row">
          <span className="form-label">Einheiten</span>
          <input
            type="text"
            placeholder="Einheiten"
            value={einheiten}
            onChange={(e) => setEinheiten(e.target.value)}
          />
        </div>
        {/* Standort */}
        <div className="form-row">
          <span className="form-label">ProductCode</span>
          <input
            type="text"
            placeholder="ProductCode"
            value={productCode}
            onChange={(e) => setProductCode(e.target.value)}
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

export default Lizenzhinzufuegen;
