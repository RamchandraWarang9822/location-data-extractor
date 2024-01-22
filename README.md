# Location Data Extractor

Location Data Extractor is a user-friendly web application that simplifies the search for places of interest using the Google Maps API. Discover nearby locations effortlessly, explore their details, and enjoy convenient navigation with a clean and responsive interfaceConcise project overview.

## Setup Locally with Docker

### Prerequisites

Ensure Docker is installed on your machine.

- [Docker Installation](https://docs.docker.com/get-docker/)

### 1. Clone the Repository

```bash
git clone https://github.com/RamchandraWarang9822/location-data-extractor
cd location-data-extractor
```

### 2. Build Docker Images

#### Frontend

```bash
cd frontend
docker build -t frontend .
```

#### Backend

```bash
cd ../backend
docker build -t backend .
```

### 3. Create Docker Network

```bash
docker network create location-extractor
```

### 4. Run Docker Containers

#### Frontend

```bash
docker run --rm --name frontend --network location-extractor -p 5173:5173 frontend
```

#### Backend

```bash
docker run --name backend --rm --network location-extractor -p 8000:8000 backend
```

### 5. Access the Application

The frontend will be available at [http://localhost:5173](http://localhost:5173).

The backend will be available at [http://localhost:8000](http://localhost:8000).

### 6. Cleanup

To stop and remove the running containers:

```bash
docker stop frontend backend
docker network rm location-extractor
```

## Additional Notes

- Include any additional notes or instructions here.