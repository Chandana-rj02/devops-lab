<<<<<<< HEAD

# Real-Time Monitoring of a Quick-Commerce App

## Objective
Build a real-time delivery monitoring system using Python,
Prometheus, Grafana, Docker, and Jenkins.

## Technologies
- Python
- Prometheus
- Grafana
- Docker and Docker Compose
- Jenkins
- Git and GitHub

## Features
- Simulates delivery metrics every second.
- Exposes metrics through an HTTP endpoint.
- Collects metrics using Prometheus.
- Displays delivery metrics in Grafana dashboards.
- Defines alerts for high pending deliveries and
  high average delivery time.
- Includes a Jenkins pipeline for validation and Docker builds.

## Project Structure
- delivery_metrics.py - Generates simulated delivery metrics.
- prometheus.yml - Configures Prometheus scraping.
- alert_rules.yml - Defines alert rules.
- Dockerfile - Builds the Python application image.
- docker-compose.yml - Starts all monitoring services.
- Jenkinsfile - Defines the CI pipeline.
- README.md - Project documentation.

## How to Run
1. Install Docker Desktop.
2. Start Docker Desktop.
3. Open a terminal in the project directory.
4. Run:

   docker compose up -d --build

## Access Services
- Metrics: http://localhost:8000/metrics
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

## Cleanup
Run the following command to stop and remove the containers:

    docker compose down
=======
# Real-Time Delivery Monitoring System

## 📌 Project Overview

The Real-Time Delivery Monitoring System is a containerized application that monitors delivery-related metrics using **Python, Docker, Prometheus, and Grafana**. It collects delivery statistics, exposes metrics for monitoring, and provides a dashboard for visualizing delivery performance.

## 🎯 Objectives

- Monitor total and pending deliveries.
- Track deliveries that are currently on the way.
- Measure average delivery time.
- Visualize real-time metrics using Grafana.
- Configure monitoring and alerting using Prometheus.

## 🛠️ Technologies Used

- **Python** – Generates and exposes delivery metrics.
- **Docker** – Containerizes the application.
- **Docker Compose** – Runs the application and monitoring services together.
- **Prometheus** – Collects and stores monitoring metrics.
- **Grafana** – Visualizes metrics through dashboards.
- **YAML** – Configures Prometheus, Docker Compose, and alert rules.

## ✨ Features

- Delivery metrics exposed through a Python application.
- Prometheus metrics endpoint.
- Monitoring of total deliveries.
- Tracking of pending deliveries.
- Tracking of on-the-way deliveries.
- Average delivery time monitoring.
- Grafana dashboard for visualizing metrics.
- Prometheus alert rules for monitoring delivery conditions.
- Containerized deployment using Docker Compose.

## 📂 Project Structure

```text
delivery_monitoring/
├── delivery_metrics.py
├── Dockerfile
├── compose.yaml
├── prometheus.yml
├── alert_rules.yml
├── requirements.txt
└── .gitignore
```

## ⚙️ Prerequisites

Install the following tools before running the project:

- Docker Desktop
- Git
- A web browser

Make sure Docker Desktop is running.

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Chandana-rj02/delivery-monitoring-grafana.git
```

### 2. Navigate to the project directory

```bash
cd delivery-monitoring-grafana
```

### 3. Start the application

```bash
docker compose up --build -d
```

### 4. Check the running containers

```bash
docker compose ps
```

### 5. Access the services

| Service | URL | Purpose |
|---|---|---|
| Delivery Metrics | http://localhost:8000/metrics | View exposed metrics |
| Prometheus | http://localhost:9090 | Query metrics and check targets |
| Grafana | http://localhost:3000 | Visualize metrics in dashboards |

Grafana's default login is commonly `admin` for both username and password, unless the configuration has been changed.

## 📊 Monitoring Metrics

The project includes the following metrics in its Grafana dashboard:

- **Total Deliveries** – Total number of deliveries recorded.
- **Pending Deliveries** – Number of deliveries awaiting completion.
- **On-the-Way Deliveries** – Number of deliveries currently in transit.
- **Average Delivery Time** – Average delivery time calculated from the application's time metrics.

The exact metric values depend on the running application and its generated data.

## 🔍 Verification

After starting the containers:

1. Open the metrics endpoint and verify that delivery metrics are displayed.
2. Open Prometheus and navigate to **Status → Target health**.
3. Verify that the `delivery_service` target is marked **UP**.
4. Open Grafana and view the configured delivery monitoring dashboard.

## 🛑 Stop the Application

To stop and remove the containers created by Docker Compose, run:

```bash
docker compose down
```

## 🔮 Future Enhancements

- Add notifications for critical delivery conditions.
- Introduce historical delivery trend analysis.
- Integrate a database for persistent delivery records.
- Add a web interface for managing deliveries.
- Improve alerting with configurable thresholds.

## 👩‍💻 Author

**Chandana RJ**

GitHub: [Chandana-rj02](https://github.com/Chandana-rj02)

---

*This project demonstrates containerized application deployment, metrics collection, monitoring, dashboard visualization, and alert configuration using DevOps tools.*
>>>>>>> 6ef8a073e81a032c0180aa6e9176f0a3aec2cd9e
