import React from "react";
import { useAuth } from "./AuthContext";
import NavbarAdmin from "./NavbarAdmin";
import NavbarVerwalter from "./NavbarVerwalter";
import NavbarKunde from "./NavbarKunde";

const NavbarWrapper = () => {
  const { username } = useAuth();

  if (username === "admin" || username === "Admin") {
    return <NavbarAdmin />;
  } else if (username === "verwalter" || username === "Verwalter") {
    return <NavbarVerwalter />;
  } else if (username === "kunde" || username === "Kunde") {
    return <NavbarKunde />;
  } else {
    return null;
  }
};

export default NavbarWrapper;
