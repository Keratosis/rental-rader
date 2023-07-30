import React, { useEffect, useState } from 'react';
import '../CSS/Listing.css'; // Import the Listing.css file

function Listing() {
  const [listings, setListings] = useState([]);
  useEffect(() => {
    fetch('/listings')
      .then((res) => res.json())
      .then(setListings);
  }, []);

  return (
    <div>
      <h2>Listings</h2>
      <div className="property-row">
        {listings.map((listing) => (
          <div key={listing.id} className="property-col-md-6 property-col-lg-4 mb-4">
            <div className="property-card">
              <img src={listing.media} className="property-img" alt="Property Image" />
              <div className="property-details">
                <h5 className="property-title">{listing.title}</h5>
                <p className="property-text">{listing.description}</p>
                <p className="property-text">Rent: {listing.rent}</p>
                <p className="property-text">Location: {listing.place}</p>
                <p className="property-text">Utilities: {listing.utilities}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Listing;
