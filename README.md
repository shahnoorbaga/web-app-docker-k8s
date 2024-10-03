# Web App with Docker, Kubernetes, and GitHub
This project involves building a web application with Docker containers, deploying it using Kubernetes, and managing the project using GitHub.

1) Clone the repository
git clone https://github.com/shahnoorbaga/web-app-docker-k8s.git
cd web-app-docker-k8s

2) Replace backendURL with actual python backedn URL in app.js
const backendUrl = "http://localhost:5000"

3) Build Frontend and backend image
docker build -t web-app-frontend .
docker build -t web-app-backend .

4) Change docker image name in deployment.yaml and run below commands
kubectl apply -f Kubernetes/deployment.yaml
kubectl apply -f Kubernetes/service.yaml

