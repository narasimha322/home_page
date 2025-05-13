import React from "react";
import "../styles/aboutus.css"; 


const AboutUs = () => {
  return (
    <>
      <section className="about-section">
        <div className="about-container">
          <div className="about-image">
            <img src="/about-image.png" alt="Apollo Hospital" />
          </div>
          <div className="about-content">
            <h2>About Us</h2>
            <p>
              At Apollo Hospital, we are committed to providing world-class
              healthcare services using cutting-edge technology and experienced
              medical professionals. Booking doctors through our app ensures
              fast access to top specialists, reduces waiting times, and offers
              convenient appointment management from the comfort of your home.
            </p>
            <p>
              Our goal is to make healthcare more accessible, reliable, and
              patient-centric. Whether you need a general consultation,
              specialist care, or preventive check-ups, Apollo's online booking
              system helps streamline your healthcare journey.
            </p>
          </div>
        </div>
      </section>
    </>
  );
};

export default AboutUs;
