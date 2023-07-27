
# Flask Containerized App - Hello Message

Welcome to the Flask Containerized App project! This project aims to demonstrate the setup and deployment of a simple Flask web application that displays a hello message. The application is containerized using Docker, allowing for easy packaging, distribution, and execution of the app in any environment.
![docker](https://user-images.githubusercontent.com/82409763/221435713-9dfc4d09-550b-4369-8eed-4054761579a0.jpg)

# Installing Docker on the Amazon Linux server

### Pre-requisites

1. Amazon Linux EC2 Instance
2. A Docker Hub account. If you don't have one, sign up for free at https://hub.docker.com/

## Installation Steps

1. Run the following commands to install Docker

```sh
yum install docker -y
docker --version 
```   

## Starting the Docker Services
1. Run the following commands to start Docker services
```sh
# start docker services
service docker start
service docker status
``` 
# Project setup

### Create Project Directory
1. Create a new directory for your project using the following command:

```sh
mkdir myflaskapp
cd myflaskapp
```

### Create Dockerfile
1. Create a new file in directory called "Dockerfile"
Add the following content to the file:

```sh
# Use an official Python
FROM python:3.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

```

### Create a requirements.txt file

1. Create a new file in project directory called "requirements.txt"
2. Add this package in the file, one per line

```sh
Flask
```

### Create Application

1. Create a new file in project directory called "app.py"
2. Add your application code to this file

```sh
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    name = os.getenv("NAME", "World")
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 80)))

```

# Build the Docker image

1. Run the following command to build the Docker image:

```sh
docker build -t myapp .
```

2. Run the following command to check the available images

```sh
docker images
```

3. Run the following command to run a container from the image:

```sh
docker run -d -p <port>:80 --name myfirstapp myapp:latest
```

4. Run the following command to check the running container

```sh
docker ps
```
5. Testing in the Browser
    To access your Application, simply pick the public IP address of the instance and add the port number to the end of the URL
    For example http://your-ip:port-number

#  Push and Pull Docker Images from Docker Hub
### Pushing Docker Image to Docker Hub
Docker Hub is a cloud-based registry service provided by Docker that allows you to store and share Docker images with others.

Follow these steps to Push a Docker image to Docker Hub:

1. Log in to Docker Hub
2. Tag your Docker Image
Before pushing the image, you need to tag it with your Docker Hub username and the repository name.

```sh
docker tag myapp:v1 <username>/<repository>:v1
```

3. Push the Docker Image
To push the image to Docker Hub, use the following command:

```sh
docker push <username>/<repository>:v1
```
The image will be uploaded to Docker Hub, and it will be available for others to pull.

### Pulling Docker Image from Docker Hub
Follow these steps to pull a Docker image from Docker Hub:

1. Pull the Docker Image
To pull an image from Docker Hub, use the docker pull command followed by the image name and tag
```sh
docker pull my_username/my_repository:v1
``` 

# Troubleshooting
If you encounter an error while accessing your application on EC2, it may be due to the security group settings, so please ensure that the port number you are using to run the container is allowed in the inbound rules of the EC2 instance's security group.
