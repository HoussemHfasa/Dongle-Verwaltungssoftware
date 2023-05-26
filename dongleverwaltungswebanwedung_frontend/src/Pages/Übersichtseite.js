import React from "react";
import NavbarAdmin from "../Components/NavbarAdmin";
import NavbarKunde from "../Components/NavbarKunde";
import NavbarVerwalter from "../Components/NavbarVerwalter";
import { useLocation } from "react-router-dom";
import CustomTable from "./CustomTable";

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
      <table>
        <thead>
          <tr>
            <th>lfd_nr</th>
            <th>serien_nr</th>
            <th>name</th>
            <th>gueltig_von</th>
            <th>gueltig_bis</th>
            <th>projekt_produkt</th>
            <th>standort</th>
            <th>haendler</th>
            <th>datum_letzte_aenderung</th>
            <th>datum_erstausgabe</th>
            <th>benutzer_firmcode</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>SN001</td>
            <td>Example 1</td>
            <td>2023-05-01</td>
            <td>2023-05-31</td>
            <td>Product A</td>
            <td>City A</td>
            <td>Dealer A</td>
            <td>2023-05-21</td>
            <td>2023-05-01</td>
            <td>FC001</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};




export default Übersichtseite;
