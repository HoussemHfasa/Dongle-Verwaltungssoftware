import React, { useEffect, useState } from "react";
import axios from "axios";
import { Table } from "antd";
import { useAuth } from "../Components/AuthContext";

const KundeTicketTable = ({ filter, customColumns, firmcode }) => {
  const [dataSource, setDataSource] = useState([]);
  const { email, password } = useAuth();

  useEffect(() => {
    localStorage.setItem("email", email);
  }, [email]);
  useEffect(() => {
    localStorage.setItem("password", password);
  }, [password]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get(
        "http://localhost:8000/api/ticket/details/",
        {
          headers: {
            Authorization: `Basic ${btoa(`${email}:${password}`)}`,
          },
        }
      );

      const filteredData = response.data.filter(
        (ticket) => ticket.firmcode === firmcode && (!filter || filter(ticket))
      );

      setDataSource(filteredData);
      console.log("Fetched data:", response.data);
    };

    fetchData();
  }, [email, password, filter, firmcode]);

  return (
    <div>
      <Table
        columns={customColumns}
        dataSource={dataSource}
        pagination={{ pageSize: 4 }}
      />
    </div>
  );
};

export default KundeTicketTable;
