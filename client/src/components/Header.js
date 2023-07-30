
import React from 'react'
import { Link } from 'react-router-dom'; 

function Header() {
  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">RentalRader</Link>

        <div className="collapse navbar-collapse" id="navbarNavDropdown">
          <ul className="navbar-nav">
            <li className="nav-item">
              <Link className="nav-link active" to="/">Home</Link>
            </li>
            {/* <li className="nav-item dropdown">
              <a className="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink1" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Find a House
              </a>
              <ul className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink1">
                <li><a className="dropdown-item" href="#">Action</a></li>
                <li><a className="dropdown-item" href="#">Another action</a></li>
                <li><a className="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </li> */}
            {/* <li className="nav-item dropdown">
              <a className="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink2" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Why Us
              </a>
              <ul className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink2">
                <li><Link className="dropdown-item" to="/about">About</Link></li>
                <li><a className="dropdown-item" href="#">Stories</a></li>
                <li><a className="dropdown-item" href="#">Reviews</a></li>
                <li><a className="dropdown-item" href="#">Benefits</a></li>
              </ul>
            </li> */}
            <li className="nav-item">
              <Link className="nav-link" to="/search">Search</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/s">Listings</Link>
            </li>
          </ul>
        </div>

        <div className="d-flex justify-content-end">
          <a className="btn btn-outline-primary mx-2" href="/signup">Sign Up</a>
          <a className="btn btn-outline-primary" href="/login">Login</a>
        </div>
        <button className="navbar-toggler d-lg-none" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
      </div>
    </nav>
    </div>
  )
}

export default Header
