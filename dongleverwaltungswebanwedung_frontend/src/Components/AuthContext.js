import React, { createContext, useContext, useState } from "react"; // Add missing imports here

const AuthContext = createContext();

export const useAuth = () => {
  return useContext(AuthContext);
};

export const AuthProvider = ({ children }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState(() => localStorage.getItem("role") || "");

  // Include setRole function in the value object
  const value = {
    email,
    setEmail,
    password,
    setPassword,
    role,
    setRole, // Add setRole to the context
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
