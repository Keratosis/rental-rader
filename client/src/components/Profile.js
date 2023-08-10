import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import jwt_decode from 'jwt-decode'; // Import jwt-decode library
import '../CSS/Profile.css';

function Profile({ accessToken }) {
  const [userData, setUserData] = useState({});
  const [decodedToken, setDecodedToken] = useState(null); // Store decoded token

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        // Fetch user data using the specific user's API endpoint
        const response = await fetch('/users', {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        }); // Replace with the correct API endpoint
        if (!response.ok) {
          throw new Error('Failed to fetch user data.');
        }
        const user = await response.json();
        setUserData(user);

        // Decode the access token to get user details and log them
        const decoded = jwt_decode(accessToken);
        setDecodedToken(decoded);
        console.log('Decoded Token:', decoded);

        // Log the username and role
        console.log('Username:', decoded.username);
        console.log('Role:', decoded.role);
      } catch (error) {
        console.error('Error fetching user data:', error);
      }
    };

    fetchUserData();
  }, [accessToken]);
  
  return (
    <div className="profile-container">
      <div className="profile-header">
        <h2>Hi, {userData.username}!</h2>
        <div className="notifications-icon">
          {/* Replace the following line with your notifications icon or button */}
          {/* For example, you can use an SVG icon or an image */}
          <button className="notifications-button">
            <img src="notifications-icon.png" alt="Notifications" />
          </button>

          {/* You can add links to notifications, messages, or alerts */}
          <div className="notifications-dropdown">
            <ul>
              <li><Link to="/notifications">Notifications</Link></li>
              <li><Link to="/messages">Messages</Link></li>
              <li><Link to="/alerts">Alerts</Link></li>
            </ul>
          </div>
        </div>
      </div>

      <div className="profile-info">
        <h3>My Profile</h3>
        <ul>
          <li><strong>Username:</strong> {decodedToken?.username}</li>
          <li><strong>Role:</strong> {decodedToken?.role}</li>
          <li><strong>Email:</strong> {decodedToken?.email}</li>
          <li><strong>Registration Date:</strong> {userData.registrationDate}</li>
        </ul>
      </div>

      <div className="profile-actions">
        <Link to="/update-account">UPDATE ACCOUNT</Link>
        <Link to="/change-username">CHANGE USERNAME</Link>
        <Link to="/change-password">CHANGE PASSWORD</Link>
      </div>
    </div>
  );
}

export default Profile;

