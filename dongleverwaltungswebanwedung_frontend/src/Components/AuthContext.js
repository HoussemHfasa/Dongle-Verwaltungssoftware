import React, { createContext, useContext, useState } from "react";

// Authentifizierungskontext erstellen
const AuthContext = createContext();

// Benutzerdefinierter Hook, um den Authentifizierungskontext abzurufen
export const useAuth = () => {
  return useContext(AuthContext);
};

// Authentifizierungsanbieter-Komponente
export const AuthProvider = ({ children }) => {
  // Authentifizierungsstatus verwalten
  const [email, setEmail] = useState(() => localStorage.getItem("email") || "");
  const [password, setPassword] = useState(
    () => localStorage.getItem("password") || ""
  );
  const [role, setRole] = useState(() => localStorage.getItem("role") || "");
  //test
  const [Firmcode, setFirmcode] = useState("");

  // Wertobjekt für den Kontext
  const value = {
    email,
    setEmail,
    password,
    setPassword,
    role,
    setRole,
    Firmcode,
    setFirmcode,
  };

  // Authentifizierungskontext bereitstellen
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
