import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import "../styles/createstaff.css";

const CreateStaff = () => {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    phone: "",
    password: "",
  });
  const [message, setMessage] = useState("");
  const [isAdmin, setIsAdmin] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("access");
    if (token) {
      try {
        const decoded = jwtDecode(token);
        if (decoded.is_staff || decoded.is_superuser) {
          setIsAdmin(true);
        } else {
          navigate("/");
        }
      } catch (error) {
        navigate("/auth");
      }
    } else {
      navigate("/auth");
    }
  }, [navigate]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem("access");
      const response = await fetch("/api/create-staff/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setMessage("✅ Staff created successfully!");
        setFormData({ username: "", email: "", phone: "", password: "" });
      } else {
        const data = await response.json();
        const errors = Object.values(data).flat().join(" ");
        setMessage(`❌ ${errors || "Error creating staff."}`);
      }
    } catch (error) {
      setMessage("❌ Network error creating staff.");
    }
  };

  if (!isAdmin) return null;

  return (
    <section className="staff-section">
      <div className="staff-container">
        <div className="staff-image">
          <img src="/about-image.png" alt="Create Staff" />
        </div>
        <div className="staff-form">
          <h2>Create Staff</h2>
          <form onSubmit={handleSubmit}>
            <input
              name="username"
              value={formData.username}
              onChange={handleChange}
              placeholder="Username"
              required
            />
            <input
              name="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="Email"
              required
            />
            <input
              name="phone"
              value={formData.phone}
              onChange={handleChange}
              placeholder="Phone"
              required
            />
            <input
              name="password"
              type="password"
              value={formData.password}
              onChange={handleChange}
              placeholder="Password"
              required
            />
            <button type="submit">Create</button>
          </form>
          <p>{message}</p>
        </div>
      </div>
    </section>
  );
};

export default CreateStaff;
