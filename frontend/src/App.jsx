import { useState } from 'react';
import axios from 'axios';

function App() {
  const [places, setPlaces] = useState([]);
  const [location, setLocation] = useState('');
  const [keyword, setKeyword] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSearch = () => {
    setLoading(true);
    axios.get(`/api?location=${location}&keyword=${keyword}`)
      .then(res => setPlaces(res.data))
      .catch(error => console.error(error))
      .finally(() => setLoading(false));
  };

  return (
    <div className="App">
      <div>
        <label>
          Location:
          <input type="text" value={location} onChange={(e) => setLocation(e.target.value)} />
        </label>
        <label>
          Keyword:
          <input type="text" value={keyword} onChange={(e) => setKeyword(e.target.value)} />
        </label>
        <button onClick={handleSearch} disabled={loading}>
          {loading ? 'Loading...' : 'Search'}
        </button>
      </div>

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
