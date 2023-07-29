import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Listing() {
  const [listings, setListings] = useState([]);

  useEffect(() => {
    // Fetch listings from the Flask API when the component mounts
    axios.get(' http://127.0.0.1:5550/listings')
      .then(response => {
        setListings(response.data);
      })
      .catch(error => {
        console.error('Error fetching listings:', error);
      });
  }, []);

  return (
    <div>
      <h2>Listings</h2>
      <ul>
        {listings.map(listing => (
          <li key={listing.id}>
            <strong>{listing.title}</strong>
            <p>{listing.description}</p>
            {/* Add more listing details here */}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Listing;
