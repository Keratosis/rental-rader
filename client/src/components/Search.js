import React from 'react';
import "../CSS/Search.css"
import Map from './Map';


function Search() {
  return (
    <div>
      <div className="search-container">
        {/* Add your search input and button here */}
        <input type="text" placeholder="Enter location" />
        <button>Search</button>
      </div>
      <div className="map-container">
     <Map/> 
        
        {/* Placeholder for the map */}
        {/* You can integrate a map library here (e.g., Google Maps, Mapbox, Leaflet) */}
      </div>
      <div className="search-results">
        {/* Placeholder for the searched results */}
        {/* Display the search results here */}
      </div>
    </div>
  );
}

export default Search;
