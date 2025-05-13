import React from "react";
import { useNavigate } from "react-router-dom"; // Import useNavigate
import "../styles/homepage.css"; // Import your CSS file

function HomePage() {
  const navigate = useNavigate(); // Initialize useNavigate

  const handleButtonClick = () => {
    navigate("/auth"); // Redirect to /auth when button is clicked
  };

  return (
    <div>
      <section className="hero-box">
        <div className="hero-content">
          {/* Left Text */}
          <div className="hero-text">
            <h1>Book Appointment <br /> With Trusted Doctors</h1>
            <p>
              Simply browse through our extensive list of trusted doctors, <br />
              schedule your appointment hassle-free.
            </p>
            <button className="hero-button" onClick={handleButtonClick}>
              Book appointment →
            </button>
          </div>

          {/* Right Image */}
          <div className="hero-image">
            <img src="/doctor2.png" alt="Doctors" />
          </div>
        </div>
      </section>
    </div>
  );
}

export default HomePage;
