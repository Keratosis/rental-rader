
import React from 'react'

function Header() {
  return (
    <div>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      
        <a class="navbar-brand" href="">RentalRader</a>
    
        
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link active" href="" aria-current="page">Home</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink1" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Find a House
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink1">
                        <li><a class="dropdown-item" href="#">Action</a></li>
                        <li><a class="dropdown-item" href="#">Another action</a></li>
                        <li><a class="dropdown-item" href="#">Something else here</a></li>
                    </ul>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink2" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Why Us
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink2">
                        <li><a class="dropdown-item" href="{{ url_for('why_us_page')}}">About</a></li>
                        <li><a class="dropdown-item" href="#">Stories</a></li>
                        <li><a class="dropdown-item" href="#">Reviews</a></li>
                        <li><a class="dropdown-item" href="#">Benefits</a></li>
                    </ul>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="">Listings</a>
                </li>
            </ul>
        </div>
        <div class="d-flex justify-content-end">
          
          
          {/* <form class="d-flex">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
          </form> */}

           
            <a class="btn btn-outline-primary mx-2" href="">Sign Up</a>
            <a class="btn btn-outline-primary" href="
            ">Login</a>

      </div>

      <button class="navbar-toggler d-lg-none" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
      </button>
  </div>
</nav>


    </div>
  )
}

export default Header
