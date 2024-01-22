# Map Scraper 

Brief project description goes here.

## Local Setup with Docker

### Prerequisites

Make sure you have Docker installed on your machine.

- [Docker Installation](https://docs.docker.com/get-docker/)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
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
docker network create react-python
```

### 4. Run Docker Containers

#### Frontend

```bash
docker run --rm --name frontend --network react-python -p 5173:5173 frontend
```

#### Backend

```bash
docker run --name backend --rm --network react-python -p 8000:8000 backend
```

### 5. Access the Application

The frontend will be available at [http://localhost:5173](http://localhost:5173).

The backend will be available at [http://localhost:8000](http://localhost:8000).

### 6. Cleanup

To stop and remove the running containers:

```bash
docker stop frontend backend
docker network rm react-python
```

## Additional Notes

- Add any additional notes or instructions here.

```

Remember to replace placeholders like `your-username` and `your-repo` with your actual GitHub username and repository name. Also, adjust the URLs and port numbers based on your application configuration.#   m a p - s c r a p e r  
 