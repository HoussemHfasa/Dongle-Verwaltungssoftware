import { useState, useEffect } from "react";

const useRoleState = () => {
  const [role, setRole] = useState(() => localStorage.getItem("role") || "");

  useEffect(() => {
    const handleStorageChange = (e) => {
      if (e.key === "role") {
        setRole(e.newValue);
      }
    };

    window.addEventListener("storage", handleStorageChange);

    return () => {
      window.removeEventListener("storage", handleStorageChange);
    };
  }, []);

  return [role, setRole];
};

export default useRoleState;
