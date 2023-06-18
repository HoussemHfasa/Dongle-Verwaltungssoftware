import { useState, useEffect } from "react";
import axios from "axios";
import { useAuth } from "../Components/AuthContext";

const useAdminAccess = () => {
  const { email, password } = useAuth();
  const [isAdmin, setIsAdmin] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const getAdminAccessToken = async () => {
      setIsLoading(true); //Laden anzeigen
      try {
        const response = await axios.post(
          //Administratorzugriffstoken abrufen
          "http://127.0.0.1:8000/admin-access-token/",
          {
            email,
            password,
          }
        );

        if (response.status === 200) {
          setIsAdmin(true); //Benutzer ist Admin
          setIsLoading(false); //Laden ausblenden
          return response.data.access_token;
        }
      } catch (error) {
        //Fehlerbehandlung
        console.error("Error obtaining admin access token:", error.message);
        if (error.response) {
          console.error("Server response data:", error.response.data);
        }
      }

      setIsAdmin(false); //Benutzer ist kein Admin
      setIsLoading(false); //Laden ausblenden
      return null;
    };

    getAdminAccessToken();
  }, [email, password]);

  return { isAdmin, isLoading }; //Adminstatus und Ladestatus zurückgeben
};

export default useAdminAccess;
