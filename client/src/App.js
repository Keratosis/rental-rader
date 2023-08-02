import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from "./components/Header";
import Homepage from "./components/Homepage";
import Listing from "./components/Listing";
import Signup from "./components/Signup";
import Login from "./components/Login";
import Footer from "./components/Footer";
import './App.css';
import Search from "./components/Search";
import Tenantsignup from "./components/Tenantsignup";
import Ownersignup from "./components/Ownersignup";
import ProtectedRoute from './components/ProtectedRoute'; // Import the ProtectedRoute component

function App() {
  return (
    <div className="app-container">
      <Header />
      <div className="main-content">
        <Routes>
        <Route path="/" element={<ProtectedRoute component={Homepage} />} />
          <Route path="/s" element={<ProtectedRoute component={Listing} />} />
          <Route path="/signup" element={<ProtectedRoute component={Signup} />} />
          <Route path="/login" element={<ProtectedRoute component={Login} />} />
          <Route path="/search" element={<ProtectedRoute component={Search} />} />
          <Route path="/Tenantsignup" element={<ProtectedRoute component={Tenantsignup} />} />
          <Route path="/Ownersignup" element={<ProtectedRoute component={Ownersignup} />} />
        </Routes>
      </div>
      <Footer />
    </div>
  );
}




export default App;
