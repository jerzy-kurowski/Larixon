# Larixon

Welcome to the Larixon! This application is designed to help you manage bets easily and efficiently.

## Getting Started

To get started with the Larixon, follow these steps:

### Prerequisites

Ensure you have the following installed on your machine:

- Docker
- Docker Compose

### Building the Docker Compose

The application is containerized using Docker. To build and run the application, use the `local.yml` Docker Compose file provided in the repository.

1. Open your terminal.
2. Navigate to the directory containing the `local.yml` file.
3. Run the following command:

   ```sh
   docker-compose -f local.yml up --build

### Accessing the Swagger Documentation
Once the containers are up and running, you can access the Swagger documentation to explore and interact with the API.

1. Open your web browser.
2. Go to the following URL:

    ```sh 
   http://127.0.0.1:8000/api/docs/

This URL will take you to the Swagger UI, where you can see all available endpoints and test them.
