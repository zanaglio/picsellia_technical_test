FROM python:3.10-slim-buster

ENV TZ=Europe/Minsk
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

COPY worker_service/requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY worker_service /app
COPY utils /app/utils
COPY celery_app.py /app

WORKDIR /app
