# syntax=docker/dockerfile:1

FROM python:3.7-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y curl gcc libssl-dev libcurl4-openssl-dev

COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
