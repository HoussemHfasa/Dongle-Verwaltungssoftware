import React, { useEffect } from "react";
import { useAuth } from "./AuthContext";
import NavbarAdmin from "./NavbarAdmin";
import NavbarVerwalter from "./NavbarVerwalter";
import NavbarKunde from "./NavbarKunde";

const NavbarWrapper = () => {
  const { role, setRole } = useAuth();

  useEffect(() => {
    localStorage.setItem("role", role); // Update the role in localStorage whenever it changes
  }, [role]);

  if (role === "Admin") {
    return <NavbarAdmin />;
  } else if (role === "Verwalter") {
    return <NavbarVerwalter />;
  } else if (role === "Kunde") {
    return <NavbarKunde />;
  } else {
    return null;
  }
};

export default NavbarWrapper;
