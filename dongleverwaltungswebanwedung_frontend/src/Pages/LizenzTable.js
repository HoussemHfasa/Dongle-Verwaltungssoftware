import React, { useEffect, useState } from "react";
import axios from "axios";
import { Input, Table } from "antd";
import { useAuth } from "../Components/AuthContext";

// LizenzTable-Komponente
const LizenzTable = () => {
  // Zustand für die Datenquelle der Tabelle
  const [dataSource, setDataSource] = useState([]);
  const { email, password } = useAuth();

  // Daten abrufen, wenn die Komponente eingebunden wird

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get("http://127.0.0.1:8000/Lizenzseite/", {
        headers: {
          Authorization: `Basic ${btoa(`${email}:${password}`)}`,
        },
      });
      setDataSource(response.data.Lizenz);
    };

    fetchData();
  }, [email, password]);

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
      filterDropdown: ({ setSelectedKeys, selectedKeys, confirm }) => {
        return (
          <Input
            placeholder="Lizenzname suchen"
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
        return record.lizenzname.toLowerCase().includes(value.toLowerCase());
      },
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
      title: "Dongle Serien Nr",
      dataIndex: "dongle_serien_nr",
      filterDropdown: ({ setSelectedKeys, selectedKeys, confirm }) => {
        return (
          <Input
            placeholder="Dongle Serien Nr suchen"
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
        return record.dongle_serien_nr;
      },
    },
    {
      title: "Kunde",
      dataIndex: "kunde",
    },
  ];

  // Tabellenkomponente rendern
  return (
    <div>
      <Table
        columns={columns}
        dataSource={dataSource}
        pagination={{ pageSize: 7 }}
      />
    </div>
  );
};

export default LizenzTable;
