import React from 'react';
import {  Navigate } from 'react-router-dom';

const ProtectedRoute = ({ component: Component }) => {
  const isLoggedIn = !!localStorage.getItem('access_token');

  if (!isLoggedIn) {
    // Redirect to the login page if the user is not logged in
    return <Navigate to="/login" />;
  }

  // If the user is logged in, render the protected component
  return <Component />;
};

export default ProtectedRoute;