import React from 'react';
import '../CSS/Sect.css';

function Sect() {
  const sectionStyle = {
    backgroundImage: `url("https://cdn.pixabay.com/photo/2019/03/08/20/14/kitchen-living-room-4043091_640.jpg")`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    color: 'white', // Text color for the section
  };

  return (
    <div className="section" style={sectionStyle}>
      <div className="text-container">
        <h1>Rent Easy, Rent Easy</h1>
        <p>Search nearby apartments, homes, condos, offices, shops, storage units for rent</p>
        </div>
      </div>
  );
}

export default Sect;