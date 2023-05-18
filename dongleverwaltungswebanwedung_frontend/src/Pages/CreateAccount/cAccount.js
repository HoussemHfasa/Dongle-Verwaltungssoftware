import React, { useState } from 'react';
import './createAccount.css';

const CAccount = () => {
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

  return (
    <div className="createAcc-container">
      <div className="createAcc-header">
        <h1>Kunde erstellen</h1>
      </div>
      <div className="createAcc-form">
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
          <button className="save-button">Speichern</button>
        </div>
      </div>
    </div>
  );
};

export default CAccount;
