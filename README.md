# flask-app

Based on the guides:

- (Flask Book (2018))[https://habr.com/ru/articles/346306/]
- (Flask Book (2024))[https://habr.com/ru/articles/804245/]

## Environment Setup

```bash

    # create virtual environment
    python -m venv .venv --prompt .venv-flask
    source .venv/Scripts/activate

    # install dependencies and save to file
    (.venv-flask) $ pip install flask
    (.venv-flask) $ pip install python-dotenv
    (.venv-flask) $ pip freeze > requirements.txt
```

## Run Server

```bash
    # you don't need the following string in case you have .flaskenv and module python-dotenv installed
    (.venv-flask) $ export FLASK_APP=flask-app.py
    (.venv-flask) $ flask run
```

## Dockerizing Application

(dockerizing)[https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/]
