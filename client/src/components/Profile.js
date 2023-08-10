import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import '../CSS/Profile.css';
import jwt_decode from 'jwt-decode';


function Profile() {
  const [userData, setUserData] = useState({});

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        // Fetch user data using the specific user's API endpoint
        const response = await fetch('/users'); // Replace with the correct API endpoint
        if (!response.ok) {
          throw new Error('Failed to fetch user data.');
        }
        const data = await response.json();
  
        // Assuming your access token contains user information, you can decode it
        const token = localStorage.getItem('access_token');
        const decoded = jwt_decode(token);
  
        // Find the logged-in user's data in the array using the decoded username
        const loggedInUser = data.users.find(user => user.username === decoded.sub);
  
        // Handle the case where the logged-in user is not found
        if (!loggedInUser) {
          console.error('Logged-in user data not found.');
          return;
        }
  
        // Log the username and role of the logged-in user
        console.log('Logged-in User:', loggedInUser.username);
        console.log('Role:', loggedInUser.role);
  
        // Set the userData state with the fetched user data
        setUserData(loggedInUser);
      } catch (error) {
        console.error('Error fetching user data:', error);
      }
    };
  
    fetchUserData();
  }, []);
  
  

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
          <li><strong>Username:</strong> {userData.username}</li>
          <li><strong>Role:</strong> {userData.role}</li>
          <li><strong>Email:</strong> {userData.email}</li>
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

