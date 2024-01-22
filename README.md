# Location Data Extractor

Location Data Extractor is a user-friendly web application that simplifies the search for places of interest using the Google Maps API. Discover nearby locations effortlessly, explore their details, and enjoy convenient navigation with a clean and responsive interface. Concise project overview.

## Setup Locally with Docker

### Prerequisites

Ensure Docker and Docker Compose are installed on your machine.

- [Docker Installation](https://docs.docker.com/get-docker/)
- [Docker Compose Installation](https://docs.docker.com/compose/install/)

### 1. Clone the Repository

```bash
git clone https://github.com/RamchandraWarang9822/location-data-extractor
cd location-data-extractor
```

### 2. Create a .env file

Create a .env file in the root project folder and add your Google Places API key:

```bash
echo "API_KEY=your_google_places_api_key" > .env
```

Replace `your_google_places_api_key` with your actual Google Places API key.

### 3. Build and Run with Docker Compose

```bash
docker-compose up -d
```

This command will build and start the frontend and backend services in detached mode.

### 4. Access the Application

The frontend will be available at [http://localhost:5173](http://localhost:5173).

The backend will be available at [http://localhost:8000](http://localhost:8000).

### 5. Cleanup

To stop and remove the running containers:

```bash
docker-compose down
```

### Additional Notes

- Include any additional notes or instructions here.
```

This section now includes instructions for creating a .env file in the root project folder and adding the Google Places API key. Make sure to replace "your_google_places_api_key" with your actual API key in the .env file.