import React, { useState, useEffect } from "react";
import axios from "axios";
import { useAuth } from "../Components/AuthContext";
import styles from "./Navbar.module.css";

const NotificationMenu = () => {
  const { role, Firmcode } = useAuth();
  const [notifications, setNotifications] = useState([]);

  const fetchNotifications = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8000/tickets/${Firmcode}/`
      );
      setNotifications(response.data);
    } catch (error) {
      console.error("Error fetching notifications:", error);
    }
  };

  if (role === "Kunde") {
    useEffect(() => {
      fetchNotifications();
    }, []);
  }

  return (
    <div className={styles["notificationContainer"]}>
      {notifications.map((notification, index) => (
        <div key={index} className={styles["notificationItem"]}>
          <p>{notification.title}</p>
        </div>
      ))}
    </div>
  );
};

export default NotificationMenu;
