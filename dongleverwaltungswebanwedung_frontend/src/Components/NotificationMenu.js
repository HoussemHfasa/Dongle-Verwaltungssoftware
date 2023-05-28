import React, { forwardRef } from "react";
import styles from "./Navbar.module.css";

const NotificationMenu = forwardRef((props, ref) => {
  return (
    // Verwenden von forwardRef, um die ref-Instanz von außerhalb der Komponente zu verwalten
    <div className={styles["notificationContainer"]} ref={ref}>
      <div className={styles["notificationItem"]}>
        <p>Benachrichtigung 1</p>
      </div>
      <div className={styles["notificationItem"]}>
        <p>Benachrichtigung 2</p>
      </div>
      <div className={styles["notificationItem"]}>
        <p>Benachrichtigung 3</p>
      </div>
      {/* Fügen Sie bei Bedarf weitere Benachrichtigungselemente hinzu */}
    </div>
  );
});

export default NotificationMenu;
