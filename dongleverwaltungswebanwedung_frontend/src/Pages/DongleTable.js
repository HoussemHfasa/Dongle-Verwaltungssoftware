import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Input, Table } from 'antd';

// DongleTable-Komponente
const DongleTable = () => {
  // Zustand für die Datenquelle der Tabelle
  const [dataSource, setDataSource] = useState([]);

  // Daten abrufen, wenn die Komponente eingebunden wird
  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get('http://127.0.0.1:8000/homepage/');
      setDataSource(response.data.Dongle);
    };

    fetchData();
  }, []);

  // Spaltenkonfiguration für die Tabelle
  const columns = [
    // Laufende Nummer
    {
      title: 'Lfd.Nr',
      dataIndex: 'lfd_nr_field',
    },
    // Seriennummer
    {
      title: 'Serien Nr',
      dataIndex: 'serien_nr',
    },
    // Name
    {
      title: 'Name',
      dataIndex: 'name',
      // Filter-Dropdown-Konfiguration
      filterDropdown: ({ setSelectedKeys, selectedKeys, confirm }) => {
        return (
          <Input
            placeholder="Name suchen"
            value={selectedKeys[0]}
            onChange={(e) => {
              setSelectedKeys(e.target.value ? [e.target.value] : []);
            }}
            onPressEnter={() => {
              confirm();
            }}
            onBlur={() => {
              confirm();
            }}
          ></Input>
        );
      },
      // Filterfunktion
      onFilter: (value, record) => {
        return record.name.toLowerCase().includes(value.toLowerCase());
      },
    },
    // Gültig von
    {
      title: 'Gültig von',
      dataIndex: 'gueltig_von',
    },
    // Gültig bis
    {
      title: 'Gültig bis',
      dataIndex: 'gueltig_bis',
    },
    // Projekt / Produkt
    {
      title: 'Projekt / Produkt',
      dataIndex: 'projekt_produkt',
    },
    // Standort
    {
      title: 'Standort',
      dataIndex: 'standort',
    },
    // Händler
    {
      title: 'Händler',
      dataIndex: 'haendler',
    },
    // Datum der letzten Änderung
    {
      title: 'Datum letzte Änderung',
      dataIndex: 'datum_letzte_aenderung',
    },
    // Datum der Erstausgabe
    {
      title: 'Datum Erstausgabe',
      dataIndex: 'datum_erstausgabe',
    },
    // Benutzer Firmencode
    {
      title: 'Benutzer Firmcode',
      dataIndex: 'benutzer_firmcode',
    },
  ];

  // Tabellenkomponente rendern
  return (
    <div>
      <Table columns={columns} dataSource={dataSource} />
    </div>
  );
};

export default DongleTable;