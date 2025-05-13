import React from "react";
import { Routes, Route, useLocation } from "react-router-dom";
import "./App.css";

import HomePage from "./components/HomePage";
import DoctorsGrid from "./components/DoctorsGrid";
import Footer from "./components/Footer";
import NavBar from "./components/NavBar";
import AboutUs from "./components/AboutUs";
import ContactUs from "./components/ContactUs";
import AuthPage from "./components/Auth";
import ProtectedRoute from "./components/ProtectedRoute"; // Import your ProtectedRoute component
import CreateStaff from "./components/CreateStaff";
import ChangePassword from "./components/ChangePassword";
import ResetPassword from "./components/ResetPassword";

function App() {
  const location = useLocation();
  const isAuthPage = location.pathname === "/auth"; // Check if we are on the Auth page

  return (
    <div className="App">
      {/* Only show the NavBar if we are not on the /auth page */}
      {!isAuthPage && <NavBar />}

      <Routes>
        <Route path="/auth" element={<AuthPage />} />
        {/* Protected Routes */}
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <HomePage />
              <DoctorsGrid />
            </ProtectedRoute>
          }
        />
        <Route
          path="/about"
          element={
            <ProtectedRoute>
              <AboutUs />
            </ProtectedRoute>
          }
        />
        <Route
          path="/contact"
          element={
            <ProtectedRoute>
              <ContactUs />
            </ProtectedRoute>
          }
        />
        <Route
          path="/doctors"
          element={
            <ProtectedRoute>
              <DoctorsGrid />
            </ProtectedRoute>
          }
        />
        <Route
          path="/create-staff"
          element={
            <ProtectedRoute>
              <CreateStaff />
            </ProtectedRoute>
          }
        />
        <Route
          path="/change-password"
          element={
            <ProtectedRoute>
              <ChangePassword />
            </ProtectedRoute>
          }
        />
        <Route path="/reset-password" element={<ResetPassword />} />
      </Routes>

      {/* Only show Footer if not on /auth */}
      {!isAuthPage && <Footer />}
    </div>
  );
}

export default App;
