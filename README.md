# SimpleTimeService

A simple Python microservice that returns the current timestamp and the visitor's IP address in a JSON format.

## Prerequisites

- Docker installed on your machine.
- Git, installed too
- Python needs to be present
- If using Python framework to create the web-based microservice which in this case is Flask then, Flask needs to be present i.e, pip install flask, pip show flask

## Docker build Image and push to DockerHub

- docker build -t simple-time-service .
- docker run -d -p 5000:5000 simple-time-service
- Test locally, curl http://localhost:5000 
- docker login -u ..... -p ....
- docker tag simple-time-service aman2568/simple-time-service:latest
- docker push aman2568/simple-time-service:latest

## Push the code to git repository
   ```bash
   git clone https://github.com/amankc-neo/simpletimeservice.git
   cd simpletimeservice
   git init
   git add .
   git commit -m "Intial Commit"
   git push origin master
