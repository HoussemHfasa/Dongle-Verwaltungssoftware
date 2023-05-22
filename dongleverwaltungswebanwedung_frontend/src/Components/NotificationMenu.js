import React, { forwardRef } from "react";
import styles from "./NavbarKunde.module.css";

const NotificationMenu = forwardRef((props, ref) => {
  return (
    <div className={styles["notificationContainer"]} ref={ref}>
      <div className={styles["notificationItem"]}>
        <p>Notification 1</p>
      </div>
      <div className={styles["notificationItem"]}>
        <p>Notification 2</p>
      </div>
      <div className={styles["notificationItem"]}>
        <p>Notification 3</p>
      </div>
      {/* Add more notification items as needed */}
    </div>
  );
});

export default NotificationMenu;
