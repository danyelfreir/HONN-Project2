# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]


# docker build -t paymentservice:latest .
# docker run -d -p 5000:5000 --name paymentservice paymentservice --mount type=bind,source="$(pwd)"/target,target=/app