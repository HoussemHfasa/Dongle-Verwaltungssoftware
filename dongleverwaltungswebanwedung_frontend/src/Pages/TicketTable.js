import React, { useEffect, useState } from "react";
import axios from "axios";
import { Input, Table, Button } from "antd"; 
import { useAuth } from "../Components/AuthContext";

const TicketTable = () => {
    
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
        console.log("email test in tickettable", email, password);
        const response = await axios.get("http://localhost:8000/api/ticket/details/", {
            headers: {
                Authorization: `Basic ${btoa(`${email}:${password}`)}`,
            },
            });
            setDataSource(response.data);
            console.log("Fetched data:", response.data);
      };
  
      fetchData();
    }, [email, password]);


    const handleAccept = async (ticketId) => {
        try {
          console.log("Handling accept for ticketId:", ticketId);
          const response = await axios.put(
            `http://localhost:8000/api/ticket/details/${ticketId}/`,
            {
              id_ticket: ticketId,
              status: "beendet",
              admin_verwalter_id: email,
            },
            {
              headers: {
                Authorization: `Basic ${btoa(`${email}:${password}`)}`,
              },
            }
          );
          console.log("Ticket update response:", response.data);
          // Refresh the table data
          const responseData = await axios.get("http://localhost:8000/api/ticket/list/", {
            headers: {
              Authorization: `Basic ${btoa(`${email}:${password}`)}`,
            },
          });
          setDataSource(responseData.data);
        } catch (error) {
          console.error("Error updating ticket:", error);
        }
      };
      
    const columns = [
        {
          title: "ID_Ticket",
          dataIndex: "id_ticket",
        },
        {
          title: "Titel",
          dataIndex: "titel",
        },
        {
          title: "Beschreibung",
          dataIndex: "beschreibung",
        },
        {
          title: "Status",
          dataIndex: "status",
        },
        {
          title: "Erstellungsdatum",
          dataIndex: "erstellungsdatum",
        },
        {
          title: "Schliessungsdatum",
          dataIndex: "schliessungsdatum",
        },
        {
          title: "Admin/Verwalter_ID",
          dataIndex: "admin_verwalter_id",
        },
        {
          title: "Dongle_seriennumer",
          dataIndex: "dongle_seriennummer",
        },
        {
          title: "LizenzName",
          dataIndex: "lizenzname",
        },
        {
          title: "Grund_der_Ablehnung",
          dataIndex: "grund_der_ablehnung",
        },
        {
          title: "Kunde",
          dataIndex: "kunde",
        },

        {
            title: "Aktionen",
            dataIndex: "aktionen",
            render: (text, record) => {
              if (record.status === "in bearbeitung") {
                return (
                  <>
                    <Button
                      type="primary"
                      style={{ marginRight: "10px" }}
                      onClick={() => handleAccept(record.id_ticket)}
                    >
                      Akzeptieren
                    </Button>
                    <Button type="danger">Ablehnen</Button>
                  </>
                );
              }
              return null;
            },
          }
    ];
  
    
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
  
  export default TicketTable;