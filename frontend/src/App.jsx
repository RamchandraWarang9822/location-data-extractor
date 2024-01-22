import { useState } from 'react';
import axios from 'axios';
import {
  Container,
  TextField,
  Button,
  Card,
  CardContent,
  CircularProgress,
  IconButton,
  Link,
} from '@mui/material';
import PhoneIcon from '@mui/icons-material/Phone';
import MapIcon from '@mui/icons-material/Map';
import "./App.css"

function App() {
  const [places, setPlaces] = useState([]);
  const [location, setLocation] = useState('');
  const [keyword, setKeyword] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSearch = () => {
    setLoading(true);
    axios
      .get(`/api?location=${location}&keyword=${keyword}`)
      .then((res) => setPlaces(res.data))
      .catch((error) => console.error(error))
      .finally(() => setLoading(false));
  };

  const handlePhoneClick = (phoneNumber) => {
    window.location.href = `tel:${phoneNumber}`;
  };

  const handleMapClick = (url) => {
    window.open(url, '_blank');
  };

  return (
    <Container maxWidth="md">
      <div style={{ opacity: loading ? 0.5 : 1, transition: 'opacity 0.3s ease-in-out' }}>
        <TextField
          label="Location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Keyword"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          fullWidth
          margin="normal"
        />
        <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '10px' }}>
          <Button variant="contained" onClick={handleSearch} disabled={loading}>
            Search
          </Button>
        </div>
      </div>

      {loading && (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
          <CircularProgress />
        </div>
      )}

      <div>
        {places.map((place, index) => (
          <Card key={index} style={{ margin: '10px 0', opacity: loading ? 0.5 : 1, transition: 'opacity 0.3s ease-in-out' }}>
            <CardContent>
              <h2>
                {place.name}
              </h2>
              <p>
                {place.address}
              </p>
              {place.phone_number && (
                <p>
                  <IconButton onClick={() => handlePhoneClick(place.phone_number)}>
                    <PhoneIcon />
                  </IconButton>
                  <span>{place.phone_number}</span>
                </p>
              )}
              {place.url && (
                <p>
                  <IconButton onClick={() => handleMapClick(place.url)}>
                    <MapIcon />
                  </IconButton>
                  <Link href={place.url} target="_blank" rel="noopener noreferrer">
                    View on Map
                  </Link>
                </p>
              )}
            </CardContent>
          </Card>
        ))}
      </div>
    </Container>
  );
}

export default App;
