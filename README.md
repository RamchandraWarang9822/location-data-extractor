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

### 2. Build and Run with Docker Compose

```bash
docker-compose up -d
```

This command will build and start the frontend and backend services in detached mode.

### 3. Access the Application

The frontend will be available at [http://localhost:5173](http://localhost:5173).

The backend will be available at [http://localhost:8000](http://localhost:8000).

### 4. Cleanup

To stop and remove the running containers:

```bash
docker-compose down
```

### Additional Notes

- Include any additional notes or instructions here.
```

With these changes, the README.md file now emphasizes the use of Docker Compose for building and running the application. The cleanup section has also been updated to use `docker-compose down`. Feel free to adjust the content based on your preferences and specific instructions.