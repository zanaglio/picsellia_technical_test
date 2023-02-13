FROM python:3.10-slim-buster

ENV TZ=Europe/Minsk
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY ./api_service /app

WORKDIR app/

ENTRYPOINT bash run.sh