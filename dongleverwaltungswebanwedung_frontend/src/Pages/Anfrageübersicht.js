import React from "react";
import NavbarWrapper from "../Components/NavbarWrapper";
import styles from "./Adminseite.module.css";
import TicketTable from "./TicketTable";

const Lizenzanfordernantwort = () => {
  const filterZero = (ticket) => ticket.dongle_lizenz === 0;
  const filterOne = (ticket) => ticket.dongle_lizenz === 1;
  const columnsZero = [
    {
      title: "ID_Ticket",
      dataIndex: "id_ticket",
    },
    {
      title: "Status",
      dataIndex: "status",
      render: (status) => {
        return status === "angenommen" ? (
          <CheckCircleOutlined style={{ color: "green", fontSize: "24px" }} />
        ) : status === "abgelehnt" ? (
          <CloseCircleOutlined style={{ color: "red", fontSize: "24px" }} />
        ) : (
          status
        );
      },
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
      title: "Erstellungsdatum",
      dataIndex: "erstellungsdatum",
    },
    {
      title: "Schließerungsdatum",
      dataIndex: "schliessungsdatum",
    },
    {
      title: "Firmcode",
      dataIndex: "firmcode",
    },
    {
      title: "Gültig von",
      dataIndex: "gueltig_von",
    },
    {
      title: "Gültig bis",
      dataIndex: "gueltig_bis",
    },
    {
      title: "Mitarbeiter",
      dataIndex: "admin_verwalter_email",
    },
    {
      title: "Donglename",
      dataIndex: "dongle_name",
    },
    {
      title: "Dongleseriennummer",
      dataIndex: "dongle_seriennummer",
    },
    {
      title: "Projekt / Produkt",
      dataIndex: "projekt",
    },
    {
      title: "Standort",
      dataIndex: "standort",
    },
    {
      title: "Händler",
      dataIndex: "haendler",
    },
    {
      title: "Grund der Ablehnung",
      dataIndex: "grund_der_ablehnung",
    },
  ];

  const columnsOne = [
    {
      title: "ID_Ticket",
      dataIndex: "id_ticket",
    },
    {
      title: "Status",
      dataIndex: "status",
      render: (status) => {
        return status === "angenommen" ? (
          <CheckCircleOutlined style={{ color: "green", fontSize: "24px" }} />
        ) : status === "abgelehnt" ? (
          <CloseCircleOutlined style={{ color: "red", fontSize: "24px" }} />
        ) : (
          status
        );
      },
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
      title: "Erstellungsdatum",
      dataIndex: "erstellungsdatum",
    },
    {
      title: "Schließerungsdatum",
      dataIndex: "schliessungsdatum",
    },
    {
      title: "Firmcode",
      dataIndex: "firmcode",
    },
    {
      title: "Gültig von",
      dataIndex: "gueltig_von",
    },
    {
      title: "Gültig bis",
      dataIndex: "gueltig_bis",
    },
    {
      title: "Mitarbeiter",
      dataIndex: "admin_verwalter_email",
    },
    {
      title: "Lizenzname",
      dataIndex: "lizenzname",
    },
    {
      title: "Lizenzanzahl",
      dataIndex: "lizenzanzahl",
    },
    {
      title: "Einheiten",
      dataIndex: "einheiten",
    },
    {
      title: "Dongleseriennummer",
      dataIndex: "dongle_seriennummer",
    },
    {
      title: "Grund der Ablehnung",
      dataIndex: "grund_der_ablehnung",
    },
  ];

  return (
    <div className={styles.container}>
      {/* Rahmen für Navbar und Hintergrund */}
      <div className={styles.frame7}>
        {/* Navbar */}
        <NavbarWrapper />
        {/* Rechteckiger Hintergrund */}
        <div className={styles.rectanglebackground}></div>
      </div>

      <div className={`${styles["CustomuserTable"]} ${styles.tableContainer}`}>
        <h2>Anfrage für neue Dongles</h2>
        <TicketTable filter={filterZero} customColumns={columnsZero} />
        <h2>Anfrage für neue Lizenzen</h2>
        <TicketTable filter={filterOne} customColumns={columnsOne} />
      </div>
    </div>
  );
};

export default Lizenzanfordernantwort;
