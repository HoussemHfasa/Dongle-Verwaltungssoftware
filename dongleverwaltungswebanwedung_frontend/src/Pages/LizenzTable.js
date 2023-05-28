import React, { useEffect, useState } from "react";
import axios from "axios";
import { Table } from "antd";

const LizenzTable = () => {
  const [dataSource, setDataSource] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get("http://127.0.0.1:8000/Lizenzseite/");
      setDataSource(response.data.Lizenz);
    };

    fetchData();
  }, []);

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

  return (
    <div>
      <Table columns={columns} dataSource={dataSource} />
    </div>
  );
};

export default LizenzTable;
