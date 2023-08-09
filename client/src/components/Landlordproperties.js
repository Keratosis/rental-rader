// import React, { useState, useEffect } from "react";
// import axios from "axios";

// const LandlordProperties = () => {
//   const [users, setUsers] = useState([]);
//   const [properties, setProperties] = useState([]);
//   const [selectedLandlordId, setSelectedLandlordId] = useState(null);

//   useEffect(() => {
//     // Fetch users and properties from the Flask API
//     axios.get("http://localhost:5570/users")
//       .then((response) => {
//         setUsers(response.data);
//       })
//       .catch((error) => {
//         console.error("Error fetching users:", error);
//       });

//     axios.get("http://localhost:5570/properties") // Assuming the endpoint for properties is "/properties"
//       .then((response) => {
//         setProperties(response.data);
//       })
//       .catch((error) => {
//         console.error("Error fetching properties:", error);
//       });
//   }, []);

//   const handleLandlordSelect = (selectedId) => {
//     setSelectedLandlordId(selectedId);
//   };

//   return (
//     <div>
//       <h1>Landlords</h1>
//       <ul>
//         {users.map((user) => (
//           <li key={user.id} onClick={() => handleLandlordSelect(user.id)}>
//             {user.name}
//           </li>
//         ))}
//       </ul>

//       {selectedLandlordId !== null && (
//         <div>
//           <h2>Landlord Details:</h2>
//           <p>Name: {users.find((user) => user.id === selectedLandlordId).name}</p>
//           <p>Email: {users.find((user) => user.id === selectedLandlordId).email}</p>
          
//           <h2>Properties owned by {users.find((user) => user.id === selectedLandlordId).name}:</h2>
//           <ul>
//             {properties
//               .filter((property) => property.user_id === selectedLandlordId)
//               .map((property) => (
//                 <li key={property.id}>
//                   <p>Title: {property.title}</p>
//                   <p>Description: {property.description}</p>
//                 </li>
//               ))}
//           </ul>
//         </div>
//       )}
//     </div>
//   );
// };

// export default LandlordProperties;
