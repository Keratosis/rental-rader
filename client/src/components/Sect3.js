import React, { useEffect ,useState} from 'react'

function Sect3() {
    const [sect3, setSect3] = useState([]);
  
    useEffect(() => {
      fetch('/listings')
        .then((res) => res.json())
        .then((data) => setSect3(data))
        .catch((error) => console.error('Error fetching data:', error));
    }, []);
  
    
    return (
      <div className="horizontal-container">
        <div className="section2">
          {sect3.map((item) => (
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
  
  export default Sect3;
  