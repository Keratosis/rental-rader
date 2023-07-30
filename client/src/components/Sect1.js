import React, { useEffect, useState } from 'react';
import '../CSS/Sect1.css'

function Sect1() {
  const [sect1, setSect1] = useState([]);

  useEffect(() => {
    fetch('/listings')
      .then((res) => res.json())
      .then((data) => setSect1(data))
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  
  return (
    <div className="horizontal-container">
      
      <div className="section2">
      
        {sect1.map((item) => (
          
          <div key={item.id} className="small-container">
            <div className="rectangle">
              <img src={item.media} alt="Image" />
            </div>
            <p>{item.title}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Sect1;


