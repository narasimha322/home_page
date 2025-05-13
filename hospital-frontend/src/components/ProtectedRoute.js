import React from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "./AuthContext";

const ProtectedRoute = ({ children }) => {
  const { isAuthenticated, loading } = useAuth();

  if (loading) {
    return <div>Loading...</div>; // Or a proper spinner component
  }

  if (!isAuthenticated) {
    console.warn("🚫 Not authenticated. Redirecting to /auth");
    return <Navigate to="/auth" replace />;
  }

  return children;
};

export default ProtectedRoute;
