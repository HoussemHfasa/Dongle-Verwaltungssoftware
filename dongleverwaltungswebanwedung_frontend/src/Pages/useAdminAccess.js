import { useState, useEffect } from "react";
import axios from "axios";
import { useAuth } from "../Components/AuthContext";

const useAdminAccess = () => {
  const { email, password } = useAuth();
  const [isAdmin, setIsAdmin] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const getAdminAccessToken = async () => {
      setIsLoading(true);
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/admin-access-token/",
          {
            email,
            password,
          }
        );

        if (response.status === 200) {
          setIsAdmin(true);
          setIsLoading(false);
          return response.data.access_token;
        }
      } catch (error) {
        console.error("Error obtaining admin access token:", error.message);
        if (error.response) {
          console.error("Server response data:", error.response.data);
        }
      }

      setIsAdmin(false);
      setIsLoading(false);
      return null;
    };

    getAdminAccessToken();
  }, [email, password]);

  return { isAdmin, isLoading };
};

export default useAdminAccess;