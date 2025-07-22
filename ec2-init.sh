#!/bin/bash

# exec > /var/log/user-data.log 2>&1
# set -x

# Install AWS CLI v2
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "/tmp/awscliv2.zip"
apt install unzip
unzip /tmp/awscliv2.zip -d /tmp
/tmp/aws/install
export PATH=$PATH:/usr/local/bin

# Install Docker
apt update
apt install -y docker.io

# Start Docker service
systemctl start docker
systemctl enable docker

cd /home/ubuntu

# Build and run
docker build -t ollama-docker .
# docker run -d -p 8000:8000 ollama-app

docker run -d \
  --name ollama-app \
  --restart always \
  -p 8000:8000 \
  -v ollama:/root/.ollama \
  ollama-docker


curl -X POST localhost:8000/ask -d '{"prompt":"hello"}' -H "Content-Type: application/json"
