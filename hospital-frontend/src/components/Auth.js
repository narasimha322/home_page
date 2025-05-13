import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/authpage.css";
import { useAuth } from "./AuthContext";

const AuthPage = () => {
  const [mode, setMode] = useState("login");
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    phone: "",
    password: "",
    identifier: "",
  });

  const navigate = useNavigate();
  const { isAuthenticated, login } = useAuth();

  useEffect(() => {
    console.log("Auth state changed. isAuthenticated:", isAuthenticated);
    if (isAuthenticated) {
      console.log("User is authenticated. Redirecting to home...");
      navigate("/");
    }
  }, [isAuthenticated, navigate]);

  const handleChange = (e) => {
    console.log("Form input changed:", e.target.name, e.target.value);
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const endpoint =
      mode === "login"
        ? "http://localhost:8000/api/login/"
        : "http://localhost:8000/api/register/";

    const payload =
      mode === "login"
        ? {
            identifier: formData.identifier,
            password: formData.password,
          }
        : {
            username: formData.username,
            email: formData.email,
            phone: formData.phone,
            password: formData.password,
          };

    console.log("🔁 Submitting form to:", endpoint);
    console.log("📤 Payload:", payload);

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      console.log("📥 Response status:", response.status);
      const data = await response.json();
      console.log("📦 Response data:", data);

      if (!response.ok) {
        alert(data.error || "Something went wrong");
        return;
      }

      if (mode === "login") {
        if (data.access && data.refresh) {
          console.log("✅ Tokens received. Logging in...");
          login(data.access, data.refresh);
          alert("Login successful ✅");
        } else {
          console.warn("❌ Login failed: Tokens missing");
          alert("Login failed: Invalid credentials");
          return;
        }
      } else {
        alert("Registered successfully 🎉");
        setMode("login");
      }

      setFormData({
        username: "",
        email: "",
        phone: "",
        password: "",
        identifier: "",
      });
    } catch (error) {
      console.error("❌ Network Error:", error);
      alert("Network error. Please try again.");
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-left">
        <img src="/doc9.png" alt="Banner" />
        <p className="quote">"Simply all the tools my team and I need."</p>
      </div>

      <div className="auth-right">
        <div className="toggle-buttons">
          <button
            className={mode === "login" ? "active" : ""}
            onClick={() => setMode("login")}
          >
            Login
          </button>
          <button
            className={mode === "register" ? "active" : ""}
            onClick={() => setMode("register")}
          >
            Register
          </button>
        </div>

        <form onSubmit={handleSubmit} className="auth-form">
          <h2>{mode === "login" ? "Welcome back 👋" : "Create your account 🚀"}</h2>

          {mode === "register" && (
            <>
              <input
                type="text"
                name="username"
                placeholder="Username"
                value={formData.username}
                onChange={handleChange}
                required
              />
              <input
                type="email"
                name="email"
                placeholder="Email"
                value={formData.email}
                onChange={handleChange}
                required
              />
              <input
                type="text"
                name="phone"
                placeholder="Phone"
                value={formData.phone}
                onChange={handleChange}
                required
              />
            </>
          )}

          {mode === "login" && (
            <input
              type="text"
              name="identifier"
              placeholder="Email or Phone"
              value={formData.identifier}
              onChange={handleChange}
              required
            />
          )}

          <input
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            required
          />

          <button type="submit">
            {mode === "login" ? "Login" : "Register"}
          </button>

          <div className="toggle-link">
            {mode === "login" ? (
              <p>
                Don't have an account?{" "}
                <span onClick={() => setMode("register")}>Register</span>
              </p>
            ) : (
              <p>
                Already have an account?{" "}
                <span onClick={() => setMode("login")}>Login</span>
              </p>
            )}
          </div>
        </form>
      </div>
    </div>
  );
};

export default AuthPage;
