# Anime Recommendation System

![Groq](https://img.shields.io/badge/Groq-LLM-blue?logo=data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDAwMDAwIiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCI+PHBhdGggZD0iTTAgMGgyNHYyNEgwVjB6Ii8+PC9zdmc+)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Embeddings-yellow?logo=huggingface)
![Langchain](https://img.shields.io/badge/Langchain-Framework-green?logo=python)
![GCP VM](https://img.shields.io/badge/GCP%20VM-Cloud-blue?logo=googlecloud)
![Minikube](https://img.shields.io/badge/Minikube-K8s-orange?logo=kubernetes)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue?logo=docker)
![Grafana Cloud](https://img.shields.io/badge/Grafana%20Cloud-Monitoring-orange?logo=grafana)

---

## Overview

This project is an **Anime Recommendation System** that leverages state-of-the-art LLMs, embeddings, and scalable cloud infrastructure to provide personalized anime recommendations. The system is designed for robust deployment and monitoring using modern DevOps tools.

---

## Tech Stack

| Tool            | Purpose                                                                 |
|-----------------|-------------------------------------------------------------------------|
| ![Groq](https://img.shields.io/badge/-Groq-000?logo=data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDAwMDAwIiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCI+PHBhdGggZD0iTTAgMGgyNHYyNEgwVjB6Ii8+PC9zdmc+) | LLM for generating recommendations                                      |
| ![Hugging Face](https://img.shields.io/badge/-Hugging%20Face-fff?logo=huggingface) | Embedding model for semantic search                                      |
| ![Langchain](https://img.shields.io/badge/-Langchain-fff?logo=python) | Generative AI framework to interact with LLM                             |
| ![GCP VM](https://img.shields.io/badge/-GCP%20VM-fff?logo=googlecloud) | Cloud virtual machine for scalable deployment                            |
| ![Minikube](https://img.shields.io/badge/-Minikube-fff?logo=kubernetes) | Local Kubernetes cluster for app deployment                              |
| ![Streamlit](https://img.shields.io/badge/-Streamlit-fff?logo=streamlit) | UI/frontend for the app                                                  |
| ![Docker](https://img.shields.io/badge/-Docker-fff?logo=docker) | Containerization for deployment                                          |
| ![Grafana Cloud](https://img.shields.io/badge/-Grafana%20Cloud-fff?logo=grafana) | Monitoring for Kubernetes clusters                                       |

---

## Architecture

![Architecture Diagram](<img width="2988" height="641" alt="Image" src="https://github.com/user-attachments/assets/7a79bb2c-ca52-4c24-ab22-486066a1bd05" />)

---

## Features
- LLM-powered recommendations (Groq)
- Embedding-based semantic search (Hugging Face)
- Modular, scalable codebase
- Streamlit UI for user interaction
- Containerized with Docker
- Deployable on Kubernetes (Minikube, GCP VM)
- Monitored with Grafana Cloud

---

## Project Structure
```
app/           # Streamlit app
config/        # Configuration files
src/           # Core logic (data loader, recommender, etc.)
pipeline/      # Data pipeline scripts
data/          # Dataset(s)
utils/         # Utilities (logging, exceptions)
Dockerfile     # Containerization
k8s.yaml       # Kubernetes deployment
```

---

## Video Demo

[//]: # (Replace the link below with your video demo once uploaded)
[![Watch the video](https://img.shields.io/badge/Video-Demo-blue?logo=youtube)](VIDEO_LINK_HERE)

---

## Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/SriHarshitha88/anime_recommendation_system.git
   cd anime_recommendation_system
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app/app.py
   ```

---

## Docker Deployment

### Build and Run
```bash
# Build the Docker image
docker build -t anime-recommendation-system .

# Run the containerized application
docker run -p 8501:8501 anime-recommendation-system

# Access the Streamlit app at: http://localhost:8501
```

The project includes a `Dockerfile` that:
- Uses Python 3.10-slim as base image
- Installs system dependencies (build-essential, curl)
- Sets up the application with `pip install -e .`
- Exposes port 8501 for Streamlit
- Runs in headless mode for containerized environments

---

## Kubernetes Deployment

### Using Minikube (Local)
```bash
# Start Minikube
minikube start

# Apply Kubernetes deployment
kubectl apply -f k8s.yaml

# Access the application
minikube service anime-recommendation-service
```

### Using GCP VM
```bash
# Deploy to GCP VM
kubectl apply -f k8s.yaml

# Monitor with Grafana Cloud
# Configure Grafana Cloud monitoring for your Kubernetes cluster
```

---

## License

MIT 
