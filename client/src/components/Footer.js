import React from 'react'
import '../CSS/Footer.css'

function Footer() {
    return (
      <footer className="footer">
        <div className="footer-content">
          <p>&copy; 2023 Your Company. All rights reserved.</p>
          <ul className="footer-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="/s">Contact</a></li>
          </ul>
        </div>
      </footer>
    );
  }

export default Footer