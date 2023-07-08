import React, { useEffect, useState } from "react";
import axios from "axios";
import { Table, Button, Modal, Input } from "antd";
import { useAuth } from "../Components/AuthContext";

const TicketTable = ({ filter, customColumns }) => {
  const [dataSource, setDataSource] = useState([]);
  const { email, password } = useAuth();
  const [modalVisible, setModalVisible] = useState(false);
  const [ablehnungText, setAblehnungText] = useState("");
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

  const handleAccept = async (ticketId) => {
    console.log("handleAccept called with ticketId:", ticketId);
    try {
      console.log("Handling accept for ticketId:", ticketId);

      // Prepare the request body
      const requestBody = {
        id_ticket: ticketId,
        Mitarbeiter_email: email,
      };

      // Log the request body
      console.log("Request body:", requestBody);

      // Call the "/api/ticket/annehmen/" endpoint instead of "/api/ticket/details/{ticketId}/"
      const response = await axios.post(
        "http://localhost:8000/api/ticket/annehmen/",
        requestBody,
        {
          headers: {
            Authorization: `Basic ${btoa(`${email}:${password}`)}`,
          },
        }
      );
      console.log("Ticket accept response:", response.data);

      // Update local state
      setDataSource(
        dataSource.map((ticket) =>
          ticket.id_ticket === ticketId
            ? { ...ticket, status: "angenommen", admin_verwalter_email: email }
            : ticket
        )
      );
    } catch (error) {
      console.error("Error accepting ticket:", error);
    }
  };

  const handleAblehnenClick = (ticketId) => {
    setSelectedTicketId(ticketId);
    setModalVisible(true);
  };

  const handleModalSubmit = async () => {
    try {
      const requestBody = {
        id_ticket: selectedTicketId,
        grund_der_ablehnung: ablehnungText,
        status: "abgelehnt",
      };

      const response = await axios.put(
        `http://localhost:8000/api/ticket/details/${selectedTicketId}/`,
        requestBody,
        {
          headers: {
            Authorization: `Basic ${btoa(`${email}:${password}`)}`,
          },
        }
      );
      console.log("Ticket update response:", response.data);
      setDataSource(
        dataSource.map((ticket) =>
          ticket.id_ticket === selectedTicketId
            ? {
                ...ticket,
                grund_der_ablehnung: ablehnungText,
                status: "abgelehnt",
              } // Update the status in the local state as well
            : ticket
        )
      );
    } catch (error) {
      console.error("Error updating ticket:", error);
    } finally {
      setModalVisible(false);
      setAblehnungText("");
      setSelectedTicketId(null);
    }
  };
  const actionsColumn = {
    title: "Aktionen",
    dataIndex: "aktionen",
    render: (text, record) => {
      if (record.status === "offen") {
        return (
          <>
            <Button
              type="primary"
              style={{ marginRight: "10px" }}
              onClick={() => handleAccept(record.id_ticket)}
            >
              Akzeptieren
            </Button>
            <Button
              style={{
                backgroundColor: "#FF0000",
                borderColor: "#FF0000",
                color: "#FFFFFF",
                marginRight: "10px",
              }}
              onClick={() => handleAblehnenClick(record.id_ticket)}
            >
              Ablehnen
            </Button>
          </>
        );
      }
      return null;
    },
  };
  const columns = [...customColumns, actionsColumn];
  return (
    <div>
      <Table
        columns={columns}
        dataSource={dataSource}
        pagination={{ pageSize: 4 }}
      />
      <Modal
        title="Gründe für die Ablehnung"
        visible={modalVisible}
        onCancel={() => setModalVisible(false)}
        onOk={handleModalSubmit}
      >
        <Input
          value={ablehnungText}
          onChange={(e) => setAblehnungText(e.target.value)}
          placeholder="Geben Sie die Gründe für die Ablehnung ein"
        />
      </Modal>
    </div>
  );
};

export default TicketTable;
