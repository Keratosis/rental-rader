import React, { useEffect } from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

function Map() {
  const mapStyles = {
    height: '400px',
    width: '100%',
  };

  const defaultCenter = {
    lat: 40.712776,
    lng: -74.005974,
  };


  return (
    <LoadScript googleMapsApiKey="AIzaSyBaPcG3u0CdFBTHEYN8k-bKU3911d-DNhw">
      <GoogleMap
        mapContainerStyle={mapStyles}
        zoom={10}
        center={defaultCenter}
      >
        {/* Add markers for rental properties here */}
        <Marker position={{ lat: 40.712776, lng: -74.005974 }} />
      </GoogleMap>
    </LoadScript>
  );
}

export default Map;
