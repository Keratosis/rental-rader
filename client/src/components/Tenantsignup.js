import React, { useState } from 'react';
import GoogleLogin from 'react-google-login';

function Tenantsignup() {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    password: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add code to submit the form data to the server or perform any other actions
    console.log(formData);
  };

  const handleGoogleSuccess = (response) => {
    // Handle successful Google sign-in
    console.log('Google sign-in success:', response);
  };

  const handleGoogleFailure = (error) => {
    // Handle Google sign-in failure
    console.error('Google sign-in error:', error);
  };

  return (
    <div className="container">
      <h1 className="h3 mb-3 font-weight-normal">Tenant Signup</h1>
      <form onSubmit={handleSubmit}>
        {/* ... form fields ... */}
        <div className="form-group">
          <label htmlFor="firstName">First Name</label>
          <input
            type="text"
            id="firstName"
            name="firstName"
            value={formData.firstName}
            onChange={handleChange}
            className="form-control"
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="lastName">Last Name</label>
          <input
            type="text"
            id="lastName"
            name="lastName"
            value={formData.lastName}
            onChange={handleChange}
            className="form-control"
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            className="form-control"
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            className="form-control"
            required
          />
        </div>
        
        <button type="submit" className="btn btn-primary">
          Sign Up
        </button>
      </form>
      <div className="my-3">
        {/* Google Sign-In Button */}
        <GoogleLogin
          clientId="YOUR_GOOGLE_CLIENT_ID"
          buttonText="Sign Up with Google"
          onSuccess={handleGoogleSuccess}
          onFailure={handleGoogleFailure}
          cookiePolicy="single_host_origin"
        />
      </div>
    </div>
  );
}

export default Tenantsignup;
