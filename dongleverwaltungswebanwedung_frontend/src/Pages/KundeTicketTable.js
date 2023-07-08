import React, { useEffect, useState } from "react";
import axios from "axios";
import { Table, Button, Modal, Input } from "antd";
import { useAuth } from "../Components/AuthContext";

const KundeTicketTable = ({ filter, customColumns }) => {
  const [dataSource, setDataSource] = useState([]);
  const { email, password } = useAuth();
  const [modalVisible, setModalVisible] = useState(false);
  const [selectedTicketId, setSelectedTicketId] = useState(null);

  useEffect(() => {
    localStorage.setItem("email", email);
  }, [email]);
  useEffect(() => {
    localStorage.setItem("password", password);
  }, [password]);

  useEffect(() => {
    const fetchData = async () => {
      console.log("email test in tickettable", email, password);
      const response = await axios.get(
        "http://localhost:8000/api/ticket/details/",
        {
          headers: {
            Authorization: `Basic ${btoa(`${email}:${password}`)}`,
          },
        }
      );
      setDataSource(filter ? response.data.filter(filter) : response.data);
      console.log("Fetched data:", response.data);
    };

    fetchData();
  }, [email, password, filter]);

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
