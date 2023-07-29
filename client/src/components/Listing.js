import React, { useEffect, useState } from 'react';


function Listing() {
  const [listings, setListings] = useState([]);
  useEffect(() => {
    fetch('/listings')
    .then(res =>res.json())
    .then(setListings)
  }, [])

  return (
    <div>
      <h2>Listings</h2>
      <div className="row">
        {listings.map(listing => (
          <div key={listing.id} className="col-md-6 col-lg-4 mb-4">
            <div className="card">
              <img src={listing.media} className="card-img-top" alt="Property Image" />
              <div className="card-body">
                <h5 className="card-title">{listing.title}</h5>
                <p className="card-text">{listing.description}</p>
                <p className="card-text">Rent: {listing.rent}</p>
                <p className="card-text">Location: {listing.place}</p>
                <p className="card-text">Utilities: {listing.utilities}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Listing;
