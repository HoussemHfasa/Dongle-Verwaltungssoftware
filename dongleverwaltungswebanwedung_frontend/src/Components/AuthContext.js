import React, { createContext, useContext, useState } from "react";

// Authentifizierungsanbieter-Komponente
export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  // Authentifizierungsstatus verwalten
  const [email, setEmail] = useState(sessionStorage.getItem("email") || "");
  const [password, setPassword] = useState(
    sessionStorage.getItem("password") || ""
  );
  const [role, setRole] = useState(sessionStorage.getItem("role") || "");
  //test
  const [Firmcode, setFirmcode] = useState(
    sessionStorage.getItem("Firmcode") || ""
  );

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

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
};
