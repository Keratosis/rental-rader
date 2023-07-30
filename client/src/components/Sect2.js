import React, { useEffect ,useState} from 'react'

function Sect2() {
    const [sect2, setSect2] = useState([]);

    useEffect(() => {
      fetch('/listings')
        .then((res) => res.json())
        .then((data) => setSect2(data))
        .catch((error) => console.error('Error fetching data:', error));
    }, []);

    return (
        <div className="horizontal-container">
          <div className="section2">
            {sect2.map((item) => (
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

export default Sect2