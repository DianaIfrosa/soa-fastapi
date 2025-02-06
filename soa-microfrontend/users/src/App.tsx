import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./pages/Login";
import SignUp from "./pages/Signup";
import "./index.css";

const App = () => (
  <Router>
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<SignUp />} />
    </Routes>
  </Router>

);

const root = ReactDOM.createRoot(document.getElementById("app") as HTMLElement);
root.render(<App />);