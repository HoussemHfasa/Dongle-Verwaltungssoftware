

import React, { useState } from 'react';
import './Kunde_Dongle_anfordern.module.css';


function Kunde_Dongle_anfordern() {
  const [dongleID, setDongleID] = useState('');
  const [productName, setProductName] = useState('');
  const [customerName, setCustomerName] = useState('');
  const [dealer, setDealer] = useState('');
  const [expirationDate, setExpirationDate] = useState('');

  const handleDongleIDChange = (event) => {
    setDongleID(event.target.value);
  };
  const handleProductNameChange = (event) => {
    setProductName(event.target.value);
  };
  const handleCustomerNameChange = (event) => {
    setCustomerName(event.target.value);
  };
  const handleDealerChange = (event) => {
    setDealer(event.target.value);
  };
  const handleExpirationDateChange = (event) => {
    setExpirationDate(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Hier kannst du das Formular übermitteln oder weitere Aktionen ausführen
  };

  const handleReset = () => {
    setDongleID('');
    setProductName('');
    setCustomerName('');
    setDealer('');
    setExpirationDate('');
  };

  return (
    <div className="create-account-container">
      <h1 className="create-account-title">Kunde erstellen</h1>
      <form onSubmit={handleSubmit} onReset={handleReset} className="create-account-form">
        <div className="create-account-row">
          <label htmlFor="dongleID" className="create-account-label">Dongle-ID (Seriennummer):</label>
          <input type="text" id="dongleID" name="dongleID" value={dongleID} onChange={handleDongleIDChange} className="create-account-input" />
        </div>
        <div className="create-account-row">
          <label htmlFor="productName" className="create-account-label">Produktname:</label>
          <input type="text" id="productName" name="productName" value={productName} onChange={handleProductNameChange} className="create-account-input" />
        </div>
        <div className="create-account-row">
          <label htmlFor="customerName" className="create-account-label">Kundenname:</label>
          <input type="text" id="customerName" name="customerName" value={customerName} onChange={handleCustomerNameChange} className="create-account-input" />
        </div>
        <div className="create-account-row">
          <label htmlFor="dealer" className="create-account-label">Händler:</label>
          <input type="text" id="dealer" name="dealer" value={dealer} onChange={handleDealerChange} className="create-account-input" />
        </div>
        <div className="create-account-row">
          <label htmlFor="expirationDate" className="create-account-label">Ablaufdatum:</label>
          <input type="text" id="expirationDate" name="expirationDate" value={expirationDate} onChange={handleExpirationDateChange} className="create-account-input" />
        </div>
        <div className="create-account-row">
          <button type="reset" className="create-account-button create-account-reset">Stornieren</button>
          <button type="submit" className="create-account-button create-account-submit">Speichern</button>
        </div>
      </form>
    </div>
  );
}

export default Kunde_Dongle_anfordern;