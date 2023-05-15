import React from "react";
import "./Einloggen.css";
import { Link } from "react-router-dom";

const Einloggen = () => {
  return (
    <div className="frame-frame-wrapper">
      <div className="frame-frame">
        <div className="frame-overlap-group">
          <div className="frame-text-wrapper">
            Schreiben Sie Ihr Benutzername
          </div>
          <h1 className="frame-h-1">Einloggen</h1>
          <div className="frame-div">Benutzername</div>
          <img className="frame-image" alt={"Image"} src={"image-3.png"} />
          <div className="frame-text-wrapper-2">Schreiben Sie Ihr Passwrot</div>
          <div className="frame-text-wrapper-3">Passwrot vergessen?</div>
          <div className="frame-text-wrapper-4">Passwort</div>
          <img className="frame-image-4" alt={"Image"} src={"image-4.png"} />
          <img className="frame-line" alt={"Line"} src={"line-24.svg"} />
          <img className="frame-line-25" alt={"Line"} src={"line-24.svg"} />
          <div className="frame-overlap">
            <div className="frame-rectangle" />
            <div>
              <h1>Einloggen</h1>
              <Link to="/Übersichtseite">
                <button className="frame-text-wrapper-5">Anmelden</button>
              </Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
export default Einloggen;
