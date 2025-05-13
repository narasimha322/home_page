import React, { useState } from "react";

const ChangePassword = () => {
  const [data, setData] = useState({
    old_password: "",
    new_password: "",
  });
  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setData({ ...data, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem("access");
      const response = await fetch("/api/users/change-password/", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        setMessage("Password changed successfully.");
      } else {
        setMessage("Error changing password.");
      }
    } catch (error) {
      setMessage("Error changing password.");
    }
  };

  return (
    <div>
      <h2>Change Password</h2>
      <form onSubmit={handleSubmit}>
        <input name="old_password" type="password" onChange={handleChange} placeholder="Old Password" />
        <input name="new_password" type="password" onChange={handleChange} placeholder="New Password" />
        <button type="submit">Change</button>
      </form>
      <p>{message}</p>
    </div>
  );
};

export default ChangePassword;
