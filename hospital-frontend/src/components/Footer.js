// src/components/Footer.jsx
import React from "react";
import { useNavigate } from "react-router-dom";
import "../styles/footer.css";

const Footer = () => {
  const navigate = useNavigate();

  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-about">
          <h3>Apollo</h3>
          <p style={{ textAlign: "left" }}>
            Apollo Hospital is a trusted healthcare provider offering state-of-the-art medical services. Our platform allows you to book appointments with top specialists easily and efficiently.
          </p>
        </div>

        <div className="footer-links">
          <h3>Company</h3>
          <ul>
            <li onClick={() => navigate("/")}>Home</li>
            <li onClick={() => navigate("/about")}>About Us</li>
            <li onClick={() => navigate("/delivery")}>Delivery</li>
            <li onClick={() => navigate("/privacy")}>Privacy Policy</li>
          </ul>
        </div>

        <div className="footer-contact">
          <h3>Get in Touch</h3>
          <p>Phone: 8688611827</p>
          <p>Email: doctors@gmail.com</p>
        </div>
      </div>

      <div className="footer-bottom">
        <p>© 2025 Doctor Booking. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;
