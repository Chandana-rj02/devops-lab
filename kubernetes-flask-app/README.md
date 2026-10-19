# Flask Application on Kubernetes

## Project Overview
This project demonstrates how to deploy a Python Flask web application on a local Kubernetes cluster using Minikube and Docker.

## Technologies Used
- Python
- Flask
- Docker
- Kubernetes
- Minikube
- Git and GitHub

## Application Output
The application displays the following message in the browser:

`Hello from Flask on Kubernetes!`

## Project Files
- `app.py` – Flask web application.
- `Dockerfile` – Builds the Docker image.
- `deployment.yaml` – Defines the Kubernetes Deployment and NodePort Service.

## Deployment Steps
1. Start the Minikube cluster.
2. Build the Docker image for the Flask application.
3. Apply the Kubernetes configuration using `kubectl apply -f deployment.yaml`.
4. Check the running pods using `kubectl get pods`.
5. Access the application using `minikube service flask-service`.

## Result
The Flask application was successfully deployed on a local Kubernetes cluster and accessed through a web browser.
