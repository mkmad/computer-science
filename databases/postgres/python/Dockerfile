# pull official base image
FROM python:3.5

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# copy project
COPY *.py /app/
COPY *.dat /app/
COPY *.txt /app/
RUN pip install -r requirements.txt