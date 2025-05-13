// src/components/ContactUs.jsx
import React from 'react';
import '../styles/contactus.css';

const ContactUs = () => {
  return (
    <section className="contact-section">
      <div className="contact-container">
        <div className="contact-image">
          <img src="/contact.png" alt="Contact Apollo Hospital" />
        </div>
        <div className="contact-content">
          <h2>Contact Us</h2>
          <p>
            Need help or have any questions? Reach out to Apollo Hospital's support team.
            We’re here to assist you with appointments, health inquiries, and more.
          </p>
          <p><strong>Phone:</strong> +91-8688611827</p>
          <p><strong>Email:</strong> doctors@gmail.com</p>
          <p><strong>Address:</strong> 123 Apollo Road, Health City, India</p>
        </div>
      </div>
    </section>
  );
};

export default ContactUs;
