import React, { useEffect ,useState} from 'react'

function Sect3() {
  const [sect3, setListings] = useState([]);

  useEffect(() => {
    // Function to fetch the listings using the token
    const fetchListings = async () => {
      const token = localStorage.getItem('access_token');
      if (!token) {
        console.error('Token not found. User is not authenticated.');
        return;
      }

      try {
        const response = await fetch('/listings', {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch listings.');
        }

        const data = await response.json();
        setListings(data); // Updating the 'listings' state with the fetched data
        console.log(data); // Logging the fetched data to the console
      } catch (error) {
        console.error('Error fetching listings:', error);
      }
    };

    fetchListings();
  }, []);
    
    return (
      <div className="horizontal-container">
        <div className="section2">
          {sect3.map((item) => (
            <div key={item.id} className="small-container">
              <div className="rectangle">
                <img src={item.media} alt="pic" />
              </div>
              <p>{item.title}</p>
            </div>
          ))}
        </div>
      </div>
    );
  }
  
  export default Sect3;
  