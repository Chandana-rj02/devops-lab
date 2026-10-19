# Jenkins CI Automation

## Overview
This project demonstrates Continuous Integration (CI) concepts and the installation of Jenkins using Docker.

## Objectives
- Understand Continuous Integration.
- Learn the role of Jenkins in CI/CD.
- Install Jenkins using Docker.
- Access and configure the Jenkins dashboard.

## Technologies Used
- Jenkins
- Docker
- Visual Studio Code
- Git
- GitHub

## Installation Steps
1. Install Docker Desktop and make sure it is running.
2. Open the VS Code terminal.
3. Run Jenkins using the following Docker command:

   ```bash
   docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
   ```

4. Open Jenkins in your browser at `http://localhost:8080`.
5. Retrieve the initial administrator password using:

   ```bash
   docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
   ```

6. Enter the password on the Jenkins setup page.
7. Install the suggested plugins and create an administrator account.
8. Complete the setup and open the Jenkins dashboard.

## Screenshots
Screenshots of the Jenkins installation and dashboard will be added to the `screenshots` folder.

## Learning Outcomes
- Understanding Continuous Integration.
- Learning Jenkins installation and configuration.
- Using Docker to run Jenkins.
- Understanding basic CI/CD concepts.
- Managing project files using Git and GitHub.

## Conclusion
This practical demonstrates how Jenkins can be installed using Docker and used as an automation server for Continuous Integration and Continuous Delivery.