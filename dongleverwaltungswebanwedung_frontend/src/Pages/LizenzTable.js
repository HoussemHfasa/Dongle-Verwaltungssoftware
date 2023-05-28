import React, { useEffect, useState } from "react";
import axios from "axios";
import { Table } from "antd";

// LizenzTable-Komponente
const LizenzTable = () => {
  // Zustand für die Datenquelle der Tabelle
  const [dataSource, setDataSource] = useState([]);

  // Daten abrufen, wenn die Komponente eingebunden wird
  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get("http://127.0.0.1:8000/Lizenzseite/");
      setDataSource(response.data.Lizenz);
    };

    fetchData();
  }, []);

  // Spaltenkonfiguration für die Tabelle
  const columns = [
    {
      title: "Lfd.Nr",
      dataIndex: "lfd_nr_field",
    },
    {
      title: "Product Code",
      dataIndex: "productcode",
    },
    {
      title: "Lizenzname",
      dataIndex: "lizenzname",
    },
    {
      title: "Einheiten",
      dataIndex: "einheiten",
    },
    {
      title: "Gültig von",
      dataIndex: "gueltig_von",
    },
    {
      title: "Ablaufdatum",
      dataIndex: "ablaufdatum",
    },
    {
      title: "Lizenzanzahl",
      dataIndex: "lizenzanzahl",
    },
    {
      title: "Mitarbeiter",
      dataIndex: "mitarbeiter",
    },
    {
      title: "Projekt",
      dataIndex: "projekt",
    },
    {
      title: "Dongle Lfd.Nr",
      dataIndex: "dongle_lfd_nr_field",
    },
  ];

  // Tabellenkomponente rendern
  return (
    <div>
      <Table columns={columns} dataSource={dataSource} pagination={{ pageSize: 7 }} />
    </div>
  );
};

export default LizenzTable;