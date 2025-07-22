# Use an official base image with Ollama preinstalled (or start from Ubuntu and install manually)
FROM ubuntu:22.04

# Environment
ENV DEBIAN_FRONTEND=noninteractive
ENV HOME=/root

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Pre-pull your model (optional)
RUN ollama serve & sleep 5 && ollama pull mistral

# Install your app dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy your app code
COPY app.py .

# Expose ports (Ollama and your API server)
EXPOSE 11434 8000

# Start both servers when container runs
CMD ollama serve & uvicorn app:app --host 0.0.0.0 --port 8000
