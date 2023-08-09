import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from "./components/Header";
import Homepage from "./components/Homepage";
import Listing from "./components/Listing";
import Signup from "./components/Signup";
import Login from "./components/Login";
import Footer from "./components/Footer";
import './App.css'
import Search from "./components/Search";
import Tenantsignup from "./components/Tenantsignup";
import Ownersignup from "./components/Ownersignup";
import Propertydetails from "./components/Propertydetails";
import Landlords from "./components/Landlords";






function App() {

  const [listings, setListings] = useState([]);

  useEffect(() => {
    fetch('/listings') // Adjust the API endpoint as needed
      .then((res) => res.json())
      .then(setListings);
  }, []);

  return (
    <div className="app-container">
      <Header />
      <div className="main-content">
        <Routes>
          <Route path="/" element={<Homepage />} />
          <Route path="/s" element={<Listing />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/search" element={<Search />} />
          <Route path="/Tenantsignup" element={<Tenantsignup />} />
          <Route path="/Ownersignup" element={<Ownersignup />} />
          <Route path="/Propertydetails" element={<Propertydetails listings={listings} />} />
          <Route path="/Landlords" element={<Landlords />} />
        </Routes>
      </div>
      <Footer />
    </div>
  );
}

export default App;
