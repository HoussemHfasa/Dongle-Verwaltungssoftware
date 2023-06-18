import React, { useState } from "react";
import "./Lizenzhinzufügen.css";
import NavbarWrapper from "../Components/NavbarWrapper";
import axios from "axios";
import "react-datepicker/dist/react-datepicker.css";

const Lizenzhinzufuegen = () => {
  const [mitarbeiter, setMitarbeiter] = useState("");
  const [lizenzName, setLizenzName] = useState("");
  const [einheiten, setEinheiten] = useState("");
  const [productCode, setProductCode] = useState("");
  const [gültigVon, setGültigVon] = useState("");
  const [gültigBis, setGültigBis] = useState("");
  const [firmCode, setFirmCode] = useState("");
  const [projekt, setProjekt] = useState("");
  const [lizenzAnzahl, setLizenzAnzahl] = useState("");
  const [dongleSeriennummer, setDongleSeriennummer] = useState("");

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
    setDongleSeriennummer("");
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
          lizenzname: lizenzName,
          gueltig_von: formattedGültigVon,
          gueltig_bis: formattedGültigBis,
          projekt: projekt,
          einheiten: einheiten,
          productcode: productCode,
          mitarbeiter: mitarbeiter,
          firmcode: firmCode,
          lizenzanzahl: lizenzAnzahl,
          dongle_serien_nr: dongleSeriennummer,
        }
      );

      if (response.status === 201) {
        alert("Lizenz erfolgreich gespeichert!");
        resetForm();
      } else {
        alert("Fehler beim Speichern der Lizenz");
      }
    } catch (error) {
      console.error("Fehler beim Speichern der Lizenz:", error);
      alert("Fehler beim Speichern der Lizenz: " + error.message);
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
        {/* Mitarbeiter */}
        <div className="form-row">
          <span className="form-label">Mitarbeiter</span>
          <input
            type="text"
            placeholder="Mitarbeiter"
            value={mitarbeiter}
            onChange={(e) => setMitarbeiter(e.target.value)}
          />
        </div>
        {/* Lizenzname */}
        <div className="form-row">
          <span className="form-label">Lizenzname</span>
          <input
            type="text"
            placeholder="Lizenzname"
            value={lizenzName}
            onChange={(e) => setLizenzName(e.target.value)}
          />
        </div>
        {/* Einheiten */}
        <div className="form-row">
          <span className="form-label">Einheiten</span>
          <input
            type="text"
            placeholder="Einheiten"
            value={einheiten}
            onChange={(e) => setEinheiten(e.target.value)}
          />
        </div>
        {/* ProductCode */}
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
        {/* Lizenzanzahl */}
        <div className="form-row">
          <span className="form-label">Lizenzanzahl</span>
          <input
            type="text"
            placeholder="Lizenzanzahl"
            value={lizenzAnzahl}
            onChange={(e) => setLizenzAnzahl(e.target.value)}
          />
        </div>
        {/* Dongle Seriennummer */}
        <div className="form-row">
          <span className="form-label">Dongle Seriennummer</span>
          <input
            type="text"
            placeholder="Dongle Seriennummer"
            value={dongleSeriennummer}
            onChange={(e) => setDongleSeriennummer(e.target.value)}
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