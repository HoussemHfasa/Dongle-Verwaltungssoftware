import axios from "axios";
import React, { useState } from "react";
import "./LizenzAnfordern.css";
import NavbarWrapper from "../Components/NavbarWrapper";
import "react-datepicker/dist/react-datepicker.css";

const Lizenzanfordern = () => {
  const [dongleId, setDongleId] = useState("");
  const [lizenzname, setLizenzname] = useState("");
  const [tittel, setTittel] = useState("");
  const [beschreibung, setBeschreibung] = useState("");
  const [einheiten, setEinheiten] = useState("");
  const [productCode, setProductCode] = useState("");
  const [gueltig_von, setGültigVon] = useState("");
  const [gueltig_bis, setGültigBis] = useState("");
  const [firmCode, setFirmCode] = useState("");
  const [projekt, setProjekt] = useState("");
  const [lizenzAnzahl, setLizenzAnzahl] = useState("");

  // Funktion zum Zurücksetzen des Formulars
  const resetForm = () => {
    setDongleId("");
    setLizenzname("");
    setTittel("");
    setBeschreibung("");
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
      const formattedGueltigVon = new Date(gueltig_von)
        .toISOString()
        .split("T")[0];
      const formattedGueltigBis = new Date(gueltig_bis)
        .toISOString()
        .split("T")[0];
      const response = await axios.post(
        "http://localhost:8000/api/ticket/create/",
        {
          dongle_seriennummer: dongleId,
          titel: tittel,
          beschreibung: beschreibung,
          lizenzname: lizenzname,
          erstellungsdatum: new Date().toISOString().split("T")[0],
          schliessungsdatum: new Date().toISOString().split("T")[0],
          gueltig_von: formattedGueltigVon,
          gueltig_bis: formattedGueltigBis,
          projekt: projekt,
          einheiten: einheiten,
          productcode: productCode,
          firmcode: firmCode,
          lizenzanzahl: lizenzAnzahl,
          
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
            value={gueltig_von}
            onChange={(e) => setGültigVon(e.target.value)}
          />
        </div>
        {/* Gültig bis */}
        <div className="form-row">
          <span className="form-label">Gültig bis</span>
          <input
            type="date"
            placeholder="yyyy-mm-dd"
            value={gueltig_bis}
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
