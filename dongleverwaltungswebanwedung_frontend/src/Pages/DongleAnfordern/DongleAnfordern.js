import React, { useState } from 'react';
import './DongleAnfordern.css';

const DongleAnfordern = () => {
  const [dongleId, setDongleId] = useState('');
  const [productName, setProductName] = useState('');
  const [kundenName, setKundenName] = useState('');
  const [handler, setHandler] = useState('');
  const [ablaufdatum, setAblaufdatum] = useState('');

  const resetForm = () => {
    setDongleId('');
    setProductName('');
    setKundenName('');
    setHandler('');
    setAblaufdatum('');
  };

  const handleSave = async () => {
    const data = {
      title: productName,
      dongleId,
      handler,
      kundenName,
      ablaufdatum,
    };

    try {
      const response = await fetch('/api/create_ticket/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        const responseData = await response.json();
        console.log('Ticket erstellt:', responseData);
        resetForm();
        alert('Ticket erfolgreich erstellt!');
      } else {
        console.error('Fehler beim Erstellen des Tickets:', response);
        alert('Fehler beim Erstellen des Tickets');
      }
    } catch (error) {
      console.error('Fehler beim Erstellen des Tickets:', error);
      alert('Fehler beim Erstellen des Tickets');
    }
  };

  return (
    <div className="DongleAnfordern-container">
      <div className="DongleAnfordern-header">
        <h1>Kunde erstellen</h1>
      </div>
      <div className="DongleAnfordern-form">
        <div className="form-row">
          <span className="form-label">Dongle-ID(Seriennummer)</span>
          <input type="text" placeholder=" " value={dongleId} onChange={(e) => setDongleId(e.target.value)} />
        </div>
        <div className="form-row">
          <span className="form-label">Produktname</span>
          <input type="text" placeholder=" " value={productName} onChange={(e) => setProductName(e.target.value)} />
        </div>
        <div className="form-row">
          <span className="form-label">Kundenname</span>
          <input type="text" placeholder=" " value={kundenName} onChange={(e) => setKundenName(e.target.value)} />
        </div>
        <div className="form-row">
          <span className="form-label">Händler</span>
          <input type="text" placeholder=" " value={handler} onChange={(e) => setHandler(e.target.value)} />
        </div>
        <div className="form-row">
          <span className="form-label">Ablaufdatum</span>
          <input type="text" placeholder=" " value={ablaufdatum} onChange={(e) => setAblaufdatum(e.target.value)} />
        </div>
        <div className="button-container">
          <button className="cancel-button" onClick={() => resetForm()}>Stornieren</button>
          <button className="save-button" onClick={() => handleSave()}>Speichern</button>
        </div>
      </div>
    </div>
  );
};

export default DongleAnfordern;