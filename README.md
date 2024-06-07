# Simple Flask Application

Based on the guides:

- [Mega Flask Book (2018)](https://habr.com/ru/articles/346306/)
- [Mega Flask Book (2024)](https://habr.com/ru/articles/804245/)
- [Dockerizing flask app](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/)

## Environment Setup

```bash

    # 1. create virtual environment
    python -m venv .venv --prompt .venv-flask
    source .venv/Scripts/activate

    # 2. optional - after creating virtual environment - you may update pip
    (.venv-flask) $ python -m pip install --upgrade pip

    # 3a. optional - if dependencies are not installed - install them and
    #     save dependencies list to file
    (.venv-flask) $ pip install flask
    (.venv-flask) $ pip install python-dotenv
    (.venv-flask) $ pip freeze > requirements.txt

    # 3b. install dependencies from file
    (.venv-flask) $ pip install -r requirements.txt
```

## Run Development Server

```bash
    # you don't need the following line in case you have .flaskenv file and
    #  module python-dotenv installed
    (.venv-flask) $ export FLASK_APP=flask-app.py

    # run development server
    (.venv-flask) $ flask run
```

## Dockerizing Application

```bash
    # build docker image with the specified name
    docker build -t flask-app .

    # view docker image history
    docker image history flask-app

    # run new container with docker (interactive mode)
    docker run --name flask-app-container flask-app
    # run new container with docker (background mode)
    docker run -d  --name flask-app-container flask-app

    # start existing stopped(!) container
    docker start flask-app-container
    # stop existing started(!) container
    docker stop flask-app-container

    # open a shell inside a running(!) container
    docker exec -it flask-app-container sh

    # remove stopped(!) container
    docker rm flask-app-container

    # run the service via docker-compose
    docker-compose up
    # run the service in the background
    docker compose up -d
    # run the service with rebuild
    docker compose up --build
```
