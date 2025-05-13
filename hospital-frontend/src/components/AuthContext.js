import React, { createContext, useContext, useState, useEffect } from "react";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true); // <-- add loading state

  useEffect(() => {
    const access = localStorage.getItem("access");
    // Optionally verify token here with backend
    if (access) {
      console.log("🔍 Found access token, assuming authenticated");
      setIsAuthenticated(true);
    }
    setLoading(false); // Finish loading
  }, []);

  const login = (accessToken, refreshToken) => {
    if (accessToken && refreshToken) {
      console.log("💾 Storing tokens in localStorage");
      localStorage.setItem("access", accessToken);
      localStorage.setItem("refresh", refreshToken);
      setIsAuthenticated(true);
    } else {
      console.warn("❌ login() called without valid tokens");
    }
  };

  const logout = () => {
    console.log("🔓 Logging out...");
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
