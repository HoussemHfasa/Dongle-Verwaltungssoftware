import React, { useEffect } from "react";
import { useAuth } from "./AuthContext";
import NavbarAdmin from "./NavbarAdmin";
import NavbarVerwalter from "./NavbarVerwalter";
import NavbarKunde from "./NavbarKunde";

const NavbarWrapper = () => {
  // Auth Context verwenden, um die Benutzerrolle abzurufen
  const { role } = useAuth();

  // Rolle im localStorage speichern, wenn sie sich ändert
  useEffect(() => {
    localStorage.setItem("role", role);
  }, [role]);

  // Entscheiden, welche Navbar-Komponente basierend auf der Benutzerrolle anzuzeigen ist
  if (role === "Admin") {
    return <NavbarAdmin />;
  } else if (role === "Verwalter") {
    return <NavbarVerwalter />;
  } else if (role === "Kunde") {
    return <NavbarKunde />;
  } else {
    // Keine Navbar-Komponente anzeigen, wenn keine Rolle vorhanden ist
    return null;
  }
};

export default NavbarWrapper;
