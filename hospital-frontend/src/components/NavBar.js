import React from "react";
import { useNavigate, useLocation } from "react-router-dom";
import "../styles/navbar.css";
import { useAuth } from "./AuthContext";
import {jwtDecode} from "jwt-decode"; // Needed to decode the JWT

function NavBar() {
  const navigate = useNavigate();
  const location = useLocation();
  const { isAuthenticated, logout } = useAuth();

  const isActive = (path) => location.pathname === path;

  const handleLogout = () => {
    logout();
    navigate("/auth");
  };

  // Check if user is staff or superuser
  let isAdmin = false;
  const token = localStorage.getItem("access");

  if (token) {
    try {
      const decoded = jwtDecode(token);
      isAdmin = decoded.is_staff || decoded.is_superuser;
    } catch (error) {
      console.error("Invalid token", error);
    }
  }

  return (
    <div style={{ position: "sticky", top: 0, zIndex: 1000 }}>
      <nav className="navbar">
        <div className="navbar-left" onClick={() => navigate("/")}>
          <img src="./logo.png" alt="Logo" className="logo" />
          <h1 style={{ color: "rgb(95 111 255)", marginLeft: "8px" }}>Appolo</h1>
        </div>

        <div className="navbar-center">
          <span
            onClick={() => navigate("/")}
            className={`nav-link ${isActive("/") ? "active" : ""}`}
          >
            Home
          </span>
          <span
            onClick={() => navigate("/doctors")}
            className={`nav-link ${isActive("/doctors") ? "active" : ""}`}
          >
            All Doctors
          </span>
          <span
            onClick={() => navigate("/about")}
            className={`nav-link ${isActive("/about") ? "active" : ""}`}
          >
            About Us
          </span>
          <span
            onClick={() => navigate("/contact")}
            className={`nav-link ${isActive("/contact") ? "active" : ""}`}
          >
            Contact
          </span>
          {isAuthenticated && isAdmin && (
            <span
              onClick={() => navigate("/create-staff")}
              className={`nav-link ${isActive("/create-staff") ? "active" : ""}`}
            >
              Create Staff
            </span>
          )}
        </div>

        <div className="navbar-right">
          {isAuthenticated ? (
            <button className="logout-btn" onClick={handleLogout}>
              Logout
            </button>
          ) : (
            <button className="login-btn" onClick={() => navigate("/auth")}>
              Login/Register
            </button>
          )}
        </div>
      </nav>
    </div>
  );
}

export default NavBar;
