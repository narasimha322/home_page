import React, { useState } from "react";

const ResetPassword = () => {
  const [data, setData] = useState({
    email_or_phone: "",
    new_password: "",
  });
  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setData({ ...data, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("/api/users/reset-password/", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        setMessage("Password reset successful.");
      } else {
        setMessage("Error resetting password.");
      }
    } catch (error) {
      setMessage("Error resetting password.");
    }
  };

  return (
    <div>
      <h2>Reset Password</h2>
      <form onSubmit={handleSubmit}>
        <input name="email_or_phone" onChange={handleChange} placeholder="Email or Phone" />
        <input name="new_password" type="password" onChange={handleChange} placeholder="New Password" />
        <button type="submit">Reset</button>
      </form>
      <p>{message}</p>
    </div>
  );
};

export default ResetPassword;
