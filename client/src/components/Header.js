import React from 'react';
import { Link } from 'react-router-dom';

function Header({ isAuthenticated, username }) {
  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">
            RentalRader
          </Link>

          <div className="collapse navbar-collapse" id="navbarNavDropdown">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link active" to="/">
                  Home
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/search">
                  Search
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/listings">
                  Listings
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/properties">
                  Properties
                </Link>
              </li>
            </ul>
          </div>

          <div className="d-flex justify-content-end">
            {/* Conditionally render links based on the authentication status */}
            {!isAuthenticated && (
              <>
                <Link className="btn btn-outline-primary mx-2" to="/signup">
                  Sign Up
                </Link>
                <Link className="btn btn-outline-primary" to="/login">
                  Login
                </Link>
              </>
            )}

            {isAuthenticated && (
              <Link className="btn btn-outline-primary" to="/userdashboard">
                WELCOME {username}
              </Link>
            )}
          </div>
          <button
            className="navbar-toggler d-lg-none"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNavDropdown"
            aria-controls="navbarNavDropdown"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
        </div>
      </nav>
    </div>
  );
}

export default Header;
