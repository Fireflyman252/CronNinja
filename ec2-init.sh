#!/bin/bash

# exec > /var/log/user-data.log 2>&1
# set -x

# Install AWS CLI v2
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "/tmp/awscliv2.zip"
apt install unzip
unzip /tmp/awscliv2.zip -d /tmp
/tmp/aws/install
export PATH=$PATH:/usr/local/bin

python3 -m venv venv
source venv/bin/activate

pip install fastapi uvicorn transformers torch

uvicorn app:app --host 0.0.0.0 --port 8000

curl -X POST localhost:8000/ask -d '{"prompt":"hello"}' -H "Content-Type: application/json"
