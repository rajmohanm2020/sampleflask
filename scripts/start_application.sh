#!/bin/bash
cd /home/ubuntu/flask-employee-app

docker build -t flask-employee-api:latest .

docker run -d \
  --name flask-api \
  --restart always \
  -p 5000:5000 \
  flask-employee-api:latest