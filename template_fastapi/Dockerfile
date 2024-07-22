FROM python:3.12-slim-bullseye

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

CMD gunicorn app:app -c gunicorn_config.py
