# Calculator API with CI/CD

Production-ready Calculator API built with:

- FastAPI
- Pytest
- Docker
- Jenkins CI/CD

## Run locally

uvicorn app.main:app --reload

## Run tests

pytest

## Docker

docker build -t calculator-api .
docker run -p 8000:8000 calculator-api

## CI/CD

Jenkins pipeline automatically:
- Runs tests
- Builds Docker image
- Pushes to DockerHub
- Deploys container

