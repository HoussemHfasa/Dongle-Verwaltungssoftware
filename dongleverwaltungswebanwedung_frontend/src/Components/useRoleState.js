import { useState, useEffect } from "react";

const useRoleState = () => {
  // Initialisieren des role-States mit dem Wert aus dem localStorage oder einem leeren String
  const [role, setRole] = useState(() => localStorage.getItem("role") || "");

  // Effect zum Abhören von Änderungen im localStorage
  useEffect(() => {
    // Funktion zum Behandeln von Änderungen im localStorage
    const handleStorageChange = (e) => {
      if (e.key === "role") {
        setRole(e.newValue);
      }
    };

    // Fügen Sie den Event-Listener zum window-Objekt hinzu
    window.addEventListener("storage", handleStorageChange);

    // Entfernen Sie den Event-Listener, wenn die Komponente unmountet wird
    return () => {
      window.removeEventListener("storage", handleStorageChange);
    };
  }, []);

  // Rückgabe des role-States und der setRole-Funktion
  return [role, setRole];
};

export default useRoleState;
