import React, { useEffect, useState } from 'react';
import '../CSS/Listings.css'; // Import your custom CSS file
import { Link } from 'react-router-dom';

function Listing() {
    const [listings, setListings] = useState([]);
    const [favoriteProperties, setFavoriteProperties] = useState([]);
    
    
    useEffect(() => {
        fetch('/listings')
        .then(res => res.json())
        .then(data => {
            console.log(data);
            setListings(data);
        });
    }, []);
    
    const handleLikeProperty = async (listing) => {
        if (favoriteProperties.some(favListing => favListing.id === listing.id)) {
        // Unlike the property and remove it from favorites
        setFavoriteProperties(prevFavorites => prevFavorites.filter(favListing => favListing.id !== listing.id));
        try {
            await fetch(`/fav/${listing.id}`, {
            method: 'DELETE',
            });
        } catch (error) {
            console.error('Error removing property from favorites:', error);
            // Handle error if needed
        }
        } else {
        // Like the property and add it to favorites
        setFavoriteProperties(prevFavorites => [...prevFavorites, listing]);
        try {
            await fetch('/fav', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id: listing.id }), // Send the listing ID in the request body
            });
        } catch (error) {
            console.error('Error adding property to favorites:', error);
            // Handle error if needed
        }
        }
    };
      
  return (
    <div className="custom-listings-container">
      <h2>Listings</h2>
      <div className="custom-row">
        {listings.map(listing => (
          <div key={listing.id} className="custom-col-md-6 custom-col-lg-4 custom-mb-4">
            <div className="custom-card custom-listing-card">
              <div className="card-buttons">
              </div>
              <div className="image-container">
                <img src={listing.media} className="custom-card-img-top custom-listing-img" alt="Listing" />
              </div>
              <div className="custom-card-body">
                <h5 className="custom-card-title">{listing.title}</h5>
                <p className="custom-card-text">{listing.description}</p>
                <p className="custom-card-text">Rent: {listing.rent}</p>
                <p className="custom-card-text">Location: {listing.place}</p>
                <p className="custom-card-text">Utilities: {listing.utilities} 
                <div className="card-buttons">
                  <button onClick={() => handleLikeProperty(listing)}>
                    {/* Conditionally render the heart icon based on whether it's a favorite or not */}
                    {favoriteProperties.some(favProperty => favProperty.id === listing.id) ? (
                      <img src="https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678087-heart-64.png"
                        className="heart-icon liked" 
                        alt="Heart Icon" 
                      />
                    ) : (
                      <img
                        src="https://cdn4.iconfinder.com/data/icons/basic-ui-2-line/32/heart-love-like-likes-loved-favorite-64.png" 
                        className="heart-icon" 
                        alt="Heart Icon" 
                      />
                    )}
                  </button>
                  {/* Use the Link component to redirect to the ListingDetails page */}
                  <Link to={`/ListingDetails/${listing.id}`}>VIEW DETAILS</Link>
                </div>
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Listing

