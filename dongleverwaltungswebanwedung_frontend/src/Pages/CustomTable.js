import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Table } from 'antd';

const DongleTable = () => {
  const [dataSource, setDataSource] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get('http://127.0.0.1:8000/homepage/');
      setDataSource(response.data.Dongle);
    };

    fetchData();
  }, []);

  const columns = [
    {
      title: 'Lfd.Nr',
      dataIndex: 'lfd_nr_field',
    },
    {
      title: 'Serien Nr',
      dataIndex: 'serien_nr',
    },
    {
      title: 'Name',
      dataIndex: 'name',
    },
    {
      title: 'Gültig von',
      dataIndex: 'gueltig_von',
    },
    {
      title: 'Gültig bis',
      dataIndex: 'gueltig_bis',
    },
    {
      title: 'Projekt / Produkt',
      dataIndex: 'projekt_produkt',
    },
    {
      title: 'Standort',
      dataIndex: 'standort',
    },
    {
      title: 'Händler',
      dataIndex: 'haendler',
    },
    {
      title: 'Datum letzte Änderung',
      dataIndex: 'datum_letzte_aenderung',
    },
    {
      title: 'Datum Erstausgabe',
      dataIndex: 'datum_erstausgabe',
    },
    {
      title: 'Benutzer Firmcode',
      dataIndex: 'benutzer_firmcode',
    },
  ];

  return (
    <div>
      <Table columns={columns} dataSource={dataSource} />
    </div>
  );
};

export default DongleTable;