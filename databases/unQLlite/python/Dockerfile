# pull official base image
FROM python:3.7.6-slim-buster

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get -y install gcc

# copy project
COPY *.py /app/
COPY *.ipynb /app/
COPY *.txt /app/
COPY *.db  /app/
COPY *.sh /app/
COPY *.env /app/

# cache dependencies in a layer (faster builds)
# https://pythonspeed.com/articles/docker-cache-pip-downloads/
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

EXPOSE 8888
