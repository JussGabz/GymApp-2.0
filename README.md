# JUSSGYM

JUSSGYM is a gym management application designed to help users create and track their workout plans and gym routines. The platform is built using a microservices architecture to ensure scalability and maintainability.

## Features

- User authentication and authorization
- Workout plan creation and customization
- Viewing and tracking gym routines
- RESTful API for seamless integration
- Scalable microservices architecture

## Tech Stack

- **Frontend:** React with TypeScript
- **Backend:** Django Rest Framework (DRF)
- **Database:** PostgreSQL
- **Cloud Infrastructure:** AWS (EC2, S3)
- **Containerization:** Docker
- **Reverse Proxy:** Nginx

## Architecture

JUSSGYM follows a microservices-based approach:

- **Frontend Service:** A React app that communicates with the backend via REST APIs.
- **Backend Service:** A Django REST Framework API handling authentication, authorization, and data processing.
- **Database:** PostgreSQL for data storage and management.
- **Infrastructure:** Services are containerized using Docker and deployed on an AWS EC2 instance with Nginx as the reverse proxy.

## Setup and Installation

### Prerequisites

Ensure you have the following installed:

- Docker & Docker Compose
- Node.js & npm
- Python & pip
- PostgreSQL

### Clone the Repository

```sh
git clone https://github.com/yourusername/jussgym.git
cd jussgym
```

### Backend Setup

```sh
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
cp .env.example .env  # Update database credentials
python manage.py migrate
python manage.py runserver
```

### Frontend Setup

```sh
cd frontend
npm install
npm start
```

### Running with Docker

```sh
docker-compose up --build
```

## Deployment

The application is deployed on AWS using:

- EC2 for hosting the backend and frontend
- S3 for media storage
- Nginx as a reverse proxy

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For inquiries, reach out at [your email].

