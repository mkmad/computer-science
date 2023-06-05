# Build: docker build -t postgres .
FROM postgres:9.5

# set environment variables
ENV POSTGRES_PASSWORD=1234
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=postgres

# set work directory
WORKDIR /app

EXPOSE 5432