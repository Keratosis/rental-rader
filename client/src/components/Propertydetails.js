import React, { useState } from "react";
import { Container, Form, Button } from "react-bootstrap";
import axios from "axios";
import '../CSS/Propertydetails.css';

const Propertydetails = () => {
  const [image, setImage] = useState(null);
  const [media, setMedia] = useState("");
  const [description, setDescription] = useState("");
  const [rentMonth, setRentMonth] = useState("");
  const [rentAmount, setRentAmount] = useState("");
  const [location, setLocation] = useState("");
  const [utilities, setUtilities] = useState("");
  const [place, setPlace] = useState("");
  const [size, setSize] = useState("");
  const [title, setTitle] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    const rent = `${rentMonth} ${rentAmount}`;
    const propertyData = {
        image,
        media,
        description,
        rent,
        location,
        utilities,
        place,
        size,
        title,
      };
    // Handle form submission, e.g., send data to backend or perform an action
    console.log("Property Data:", { image, media, description, rent, location, utilities, place, size, title });

    axios.post("http://localhost:5570/listings", propertyData)
      .then((response) => {
        console.log(response.data);
        // Reset the form fields after successful data insertion
        setImage(null);
        setMedia("");
        setDescription("");
        setRentMonth("");
        setRentAmount("");
        setLocation("");
        setUtilities("");
        setPlace("");
        setSize("");
        setTitle("");
      })
      .catch((error) => {
        console.error("Error inserting data to server:", error);
      });
  };

  const handleImageDrop = (e) => {
    e.preventDefault();
    const file = e.dataTransfer.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setImage(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };


  return (
    <Container className="my-4">
      <h1>Create a Listing</h1>
      <Form onSubmit={handleSubmit}>
        <Form.Group>
          <Form.Label>Property Image</Form.Label>
          {/* <Form.Control
            type="text"
            placeholder="Enter image URL"
            value={image}
            onChange={(e) => setImage(e.target.value)}
            className="image-input"
          /> */}
          <div
            className="image-input"
            onDrop={handleImageDrop}
            onDragOver={(e) => e.preventDefault()}
          >
            {image ? (
              <img src={image} alt="Property" className="image-preview" />
            ) : (
              "Drag an image here"
            )}
          </div>
        </Form.Group>

        <Form.Group>
          <Form.Label>Media</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter media URL"
            value={media}
            onChange={(e) => setMedia(e.target.value)}
          />
        </Form.Group>

        <Form.Group>
          <Form.Label>Property Description</Form.Label>
          <Form.Control
            as="textarea"
            placeholder="Enter description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          />
        </Form.Group>

        <Form.Group>
          <Form.Label>Rent per Month in $</Form.Label>
          {/* <Form.Control
            type="number"
            placeholder="Enter rent per month"
            value={rent}
            onChange={(e) => setRent(e.target.value)}
          /> */}
          <div className="rent-input-container">
            <Form.Control
              type="number"
              placeholder="Amount"
              value={rentAmount}
              onChange={(e) => setRentAmount(e.target.value)}
            />
          </div>
        </Form.Group>

        <Form.Group>
          <Form.Label>Location</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter location"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
          />
        </Form.Group>

        <Form.Group>
          <Form.Label>Utilities</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter utilities"
            value={utilities}
            onChange={(e) => setUtilities(e.target.value)}
          />
        </Form.Group>

        <Form.Group>
          <Form.Label>Place</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter place"
            value={place}
            onChange={(e) => setPlace(e.target.value)}
          />
        </Form.Group>

        <Form.Group>
          <Form.Label>Size</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter size"
            value={size}
            onChange={(e) => setSize(e.target.value)}
          />
        </Form.Group>

        <Form.Group>
          <Form.Label>Title</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </Form.Group>

        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
    </Container>
  );
};

export default Propertydetails;