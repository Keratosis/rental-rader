import React from 'react'
import '../CSS/Sect.css'

function Sect() {
    return (
        <div className="section">
          <div className="image-container">
            <img src="https://images.unsplash.com/photo-1575517111478-7f6afd0973db?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGhvdXNlfGVufDB8fDB8fHww&auto=format&fit=crop&w=400&q=60" alt="Image" />
          </div>
          <div className="text-container">
            <h1>Find your Perfect rental property</h1>
            <p>find your properties with  rental rader</p>

         
          <div className='search-bar1'>
      <p>Search for properties to rent</p>
      <div className="search-container">
        <input type="text" placeholder="Enter property location" />
        <button>Search</button>
      </div>
    </div>
        </div>
        </div>
      );
    }

export default Sect