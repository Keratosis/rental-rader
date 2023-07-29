import React from "react";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from "./components/Header";
import Homepage from "./components/Homepage";
import Listing from "./components/Listing";
import Signup from "./components/Signup";
import Login from "./components/Login";



function App() {
  return (
    <div>
      <Header />
      <Routes>
         
      <Route path="/" element={<Homepage />} />
        <Route path="/s" element={<Listing />} /> 
        <Route path="/signup" element={<Signup />} /> 
        <Route path="/login" element={<Login />} /> 
        
      </Routes>
      </div>
  );
}

export default App;
