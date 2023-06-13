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
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("");
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
  console.log("AuthProvider value:", value);

  // Authentifizierungskontext bereitstellen
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
