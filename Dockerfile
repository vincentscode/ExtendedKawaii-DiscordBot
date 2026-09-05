FROM python:3.14-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y make curl gcc g++ libssl-dev libcurl4-openssl-dev graphviz graphviz-dev

COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --only-binary matplotlib --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
