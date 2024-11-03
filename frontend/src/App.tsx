import React from "react";
import logo from "./logo.svg";
import "./App.css";
import { Navigate, Route, Routes } from "react-router-dom";
import HomePage from "./pages/HomePage";
import PersonalPlantsPage from "./pages/PersonalPlantsPage";
import SignUpPage from "./pages/SignUpPage";
import LogInPage from "./pages/LogInPage";
import UploadPage from "./pages/UploadPage";
import ProfilePage from "./pages/ProfilePage";
import { useEffect, useState } from "react";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/index.html" element={<Navigate to="/" />} />
        <Route path="/profile" element={<ProfilePage></ProfilePage>} />
        <Route
          path="/myplants"
          element={<PersonalPlantsPage></PersonalPlantsPage>}
        />
        <Route path="/upload" element={<UploadPage></UploadPage>} />
        <Route path="/signup" element={<SignUpPage></SignUpPage>} />
        <Route path="/login" element={<LogInPage></LogInPage>} />
      </Routes>
    </div>
  );
}

export default App;
