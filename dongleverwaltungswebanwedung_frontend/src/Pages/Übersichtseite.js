import React from "react";
import NavbarAdmin from "../Components/NavbarAdmin";
import NavbarKunde from "../Components/NavbarKunde";
import NavbarVerwalter from "../Components/NavbarVerwalter";
import { useLocation } from "react-router-dom";

const Übersichtseite = () => {
  const location = useLocation();
  const username = location.state?.username;

  const renderNavbar = () => {
    if (username === "admin" || username === "Admin") {
      return <NavbarAdmin />;
    } else if (username === "verwalter" || username === "Verwalter") {
      return <NavbarVerwalter />;
    } else if (username === "kunde" || username === "Kunde") {
      return <NavbarKunde />;
    } else {
      return <></>;
    }
  };

  return (
    <div>
      {renderNavbar()}
      übersichtseite
    </div>
  );
};
export default Übersichtseite;
