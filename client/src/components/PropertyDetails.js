// PropertyDetails.js
import React, { useEffect, useState } from 'react';
import '../CSS/PropertyDetails.css'; // Import your custom CSS file
import { useParams } from 'react-router-dom';

function PropertyDetails({ match }) {
  const [propertyDetails, setPropertyDetails] = useState({}); // State to store fetched property details
  const [formData, setFormData] = useState({
    email: '',
    address: '',
    rating: '',
    review: '',
  });

  const [similarProperties, setSimilarProperties] = useState([]); // State to store fetched similar listings
  const { id: propertyId } = useParams();
 // Extracting the listing ID from the URL params

  useEffect(() => {
    // Fetching listings details from the server using property ID
    fetch(`/properties/${propertyId}`)
      .then(res => res.json())
      .then(data => {
        console.log(data);
        setPropertyDetails(data);
      })
      .catch(error => {
        console.error('Error fetching property details:', error);
      });
  }, [propertyId]);
 

  // Function to handle the image carousel
  const handleNextImage = () => {
    // Implementing logic to move to the next image in the carousel
    console.log('Next image');
  };

  const handlePreviousImage = () => {
    // Implementing logic to move to the previous image in the carousel
    console.log('Previous image');
  };

  const handleChange = e => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const response = await fetch('/reviews', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: 1, // Replace with the actual user ID
          listing_id: 123, // Replace with the actual listing ID
          property_id: 456, // Replace with the actual property ID
          comment: formData.review,
          review_date: new Date().toISOString().slice(0, 10), // Today's date in YYYY-MM-DD format
        }),
      });

      if (response.status === 201) {
        console.log('Review submitted successfully');
        setFormData({
          email: '',
          address: '',
          rating: '',
          review: '',
        });
      } else {
        console.error('Failed to submit review');
      }
    } catch (error) {
      console.error('Error submitting review:', error);
    }
  };

  // Function to render the listings features as list items
  const renderPropertyFeatures = () => {
    if (propertyDetails.features && propertyDetails.features.length > 0) {
      return propertyDetails.features.map((feature, index) => (
        <li key={index}>{feature}</li>
      ));
    } else {
      return <li>No features available</li>;
    }
  };

  return (
    <div className="property-details-container">
      {/* Section 1: Images */}
      <div className="image-carousel">
  <button onClick={handlePreviousImage}>&lt;</button>
  {/* Replacing the image source with the actual image URLs */}
  {propertyDetails.images && propertyDetails.images.length > 0 ? (
    propertyDetails.images.map((image, index) => (
      <img key={index} src={image} alt={`Listing ${index + 1}`} />
    ))
  ) : (
    <img src="/path/to/placeholder-image.jpg" alt="Placeholder" />
  )}
  {/* Add more images here */}
  <button onClick={handleNextImage}>&gt;</button>
</div>

      {/* Section 2: Overview */}
      <div className="overview">
        <h2>{propertyDetails.title}</h2>
        <p>{propertyDetails.address}</p>
        <p>Rent: {propertyDetails.property_rent}</p>
        <p>Property Type: {propertyDetails.property_type}</p>
        <p>Bedrooms: {propertyDetails.bedrooms}</p>
        <p>Bathrooms: {propertyDetails.bathrooms}</p>
        <p>Garage: {propertyDetails.garage}</p>
        <p>Date Posted: {propertyDetails.datePosted}</p>
      </div>

      {/* Section 3: Description */}
      <div className="description">
        <h2>Description</h2>
        <p>{propertyDetails.description}</p>
      </div>

      {/* Section 4: Property Owner */}
      <div className="property-owner">
        <h2>Property Owner Contact Information</h2>
        <p>{propertyDetails.landlord_name}</p>
        <p>{propertyDetails.contact_phone}</p>
        <p>{propertyDetails.contact_email}</p>
      </div>

      {/* Section 5: Address */}
      <div className="address">
        <h2>Address</h2>
        <p>Address: {propertyDetails.address}</p>
        <p>City: {propertyDetails.city}</p>
        <p>Neighbourhood: {propertyDetails.neighbourhood}</p>
        <p>Country: {propertyDetails.country}</p>
        <a href={propertyDetails.googleMapsLink} target="_blank" rel="noopener noreferrer">
          Open on Google Maps
        </a>
      </div>

      {/* Section 6: Property Details */}
      <div className="property-details">
        <h2>Property Details</h2>
        <p>Property ID: {propertyDetails.id}</p>
        <p>Bathrooms: {propertyDetails.bathrooms}</p>
        <p>Property Category: {propertyDetails.property_category}</p>
        <p>Garages: {propertyDetails.garage}</p>
        <p>Property Type: {propertyDetails.property_type}</p>
        <p>Posted: {propertyDetails.datePosted}</p>
        <h3>Features</h3>
        <ul>{renderPropertyFeatures()}</ul>
      </div>

      {/* Section 7: House Video Tour */}
      <div className="house-video-tour">
        <h2>House Video Tour</h2>
        <video controls>
          <source src={propertyDetails.videoURL} type="video/mp4" />
          {/* Fallback message for browsers that do not support the video tag */}
          Your browser does not support the video tag.
        </video>
      </div>
     

      {/* Section 8: Review */}
      <div className="review-form">
        <h2>Review</h2>
        <form onSubmit={handleSubmit}>
         <div className="form-group">
          <label>Email:</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
            />
        </div>
        <div className="form-group">
          <label>Address:</label>
          <input
            type="text"
            name="address"
            value={formData.address}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Rating:</label>
          <select
            name="rating"
            value={formData.rating}
            onChange={handleChange}
            required
          >
            <option value="" disabled>Select rating</option>
            <option value="5">5 Stars</option>
            <option value="4">4 Stars</option>
            <option value="3">3 Stars</option>
            <option value="2">2 Stars</option>
            <option value="1">1 Star</option>
          </select>
        </div>
        <div className="form-group">
          <label>Review:</label>
          <textarea
            name="review"
            value={formData.review}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">SUBMIT A REVIEW</button>
      </form>
    </div>

      Section 9: Similar Properties
      <div className="similar-properties">
        <h2>Similar Properties</h2>
        {similarProperties.length > 0 ? (
          similarProperties.map(property => (
            <div key={property.id}>
              <h3>{property.property_type}</h3>
              <p>{property.address}</p>
              <p>Rent: {property.property_rent}</p>
              <p>Bedrooms: {property.bedrooms}</p>
              <p>Bathrooms: {property.bathrooms}</p>
              <p>Description: {property.description}</p>
              <p>Landlord Name: {property.property_owner_name}</p>
            </div>
          ))
        ) : (
          <p>No similar properties available</p>
        )}
      </div>
    </div>

  );
};

export default PropertyDetails;