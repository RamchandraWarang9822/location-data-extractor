import { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [places, setPlaces] = useState([]);

  useEffect(() => {
    axios.get("/api").then(res => setPlaces(res.data));
  }, []);


  return (
    <div className="App">

      <div>
        {places.map((place, index) => (
          <div key={index}>
            <p><b>Name:</b> {place.name}</p>
            <p><b>Address:</b> {place.address}</p>
            <p><b>Phone Number:</b> {place.phone_number}</p>
            <p><b>URL:</b> {place.url}</p>
            <hr />
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
