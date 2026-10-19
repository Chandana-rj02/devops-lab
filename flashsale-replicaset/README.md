# Flash Sale Application Using Kubernetes ReplicaSets

## Project Overview
A Flask-based application that simulates an e-commerce flash sale. It demonstrates how Kubernetes ReplicaSets manage multiple application Pods, scale replicas, and replace deleted Pods automatically.

## Technologies Used
- Python and Flask
- Docker
- Kubernetes
- Minikube
- Git and GitHub

## Application Endpoints
- `/` — Displays the Big Sale welcome message and the Pod name.
- `/buy?user=123` — Simulates a purchase and displays the selected product and serving Pod.
- `/health` — Checks application health.

## Implementation
1. Created a Flask application.
2. Created a Docker image for the application.
3. Configured a Kubernetes ReplicaSet and Service.
4. Deployed three replicas and scaled to five.
5. Deleted one Pod and verified automatic replacement.
6. Tested the application endpoints.

## Result
The application ran successfully with five ready Pods on a single Minikube node. Kubernetes automatically replaced a deleted Pod and maintained the desired replica count.

## Learning Outcomes
- Understanding ReplicaSets and Pods.
- Scaling application replicas.
- Exposing applications through Kubernetes Services.
- Observing Kubernetes self-healing behavior.