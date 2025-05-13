import React from 'react';
import DoctorCard from './DoctorCard';
import '../styles/doctorsgrid.css'; 

const doctors = [
  {
    name: "Dr. Richard James",
    specialty: "General physician",
    image: "/doc1.png",
  },
  {
    name: "Dr. Emily Larson",
    specialty: "Gynecologist",
    image: "doc2.png",
  },
  {
    name: "Dr. Sarah Patel",
    specialty: "Dermatologist",
    image: "/doc3.png",
  },
  {
    name: "Dr. Christopher Lee",
    specialty: "Pediatricians",
    image: "/doc4.png",
  },
  {
    name: "Dr. Jennifer Garcia",
    specialty: "Neurologist",
    image: "/doc5.png",
  },
  // Add more entries as needed
];

const DoctorsGrid = () => {
  return (
    <section className="doctors-section">
      <h2>Top Doctors to Book</h2>
      <p className="subtext">Simply browse through our extensive list of trusted doctors.</p>
      <div className="doctors-grid">
        {doctors.map((doc, index) => (
          <DoctorCard key={index} {...doc} />
        ))}
      </div>
    </section>
  );
};

export default DoctorsGrid;
