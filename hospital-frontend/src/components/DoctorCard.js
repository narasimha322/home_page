import React from 'react';
import '../styles/doctorcard.css'; 

const DoctorCard = ({ name, specialty, image }) => {
  return (
    <div className="doctor-card">
      <img src={image} alt={name} className="doctor-img" />
      <div className="doctor-info">
        <p className="availability"><span className="dot"></span> Available</p>
        <h3>{name}</h3>
        <p className="specialty">{specialty}</p>
      </div>
    </div>
  );
};

export default DoctorCard;
