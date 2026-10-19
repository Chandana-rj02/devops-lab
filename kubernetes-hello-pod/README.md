# Kubernetes Exercise 1 - Hello Pod

## Objective
Deploy an Nginx container on a local Kubernetes cluster using Minikube.

## Tools Used
- Kubernetes
- Minikube
- kubectl
- Docker Desktop
- Nginx

## Implementation Steps

### 1. Start the Kubernetes Cluster
Started a local Kubernetes cluster using Minikube.

```powershell
minikube start --driver=docker
```

### 2. Create the Nginx Pod
Created a Pod named `hello-k8s` using the Nginx container image.

```powershell
kubectl run hello-k8s --image=nginx --port=80
```

### 3. Verify the Pod
Checked whether the Pod was running.

```powershell
kubectl get pods
```

### 4. Expose the Pod
Exposed the Pod using a NodePort Service.

```powershell
kubectl expose pod hello-k8s --type=NodePort --port=80
```

### 5. Access the Application
Opened the application in a web browser.

```powershell
minikube service hello-k8s
```

## Result
Successfully deployed an Nginx container on Kubernetes using Minikube and accessed the Nginx welcome page through a Kubernetes Service.

## Learning Outcomes
- Understood the basics of Kubernetes Pods and Services.
- Learned how to deploy a container using Minikube.
- Practiced basic Kubernetes commands.
- Accessed a containerized web application through a browser.