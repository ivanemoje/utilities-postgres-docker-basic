# Setting Up a PostgreSQL Container with Docker
PostgreSQL is a powerful, open-source relational database management system. In this repository, we'll walk through the process of spinning up a PostgreSQL container using Docker.

We'll also set up a basic Python project structure to interact with the database.

## Pre-requisites
- [Docker](https://www.docker.com/)

## Project Structure
First, let's set up our project structure. Create a new directory for your project and add the following files:

postgres-docker/
│
├── .gitignore
├── Dockerfile
├── main.py
├── requirements.txt
└── database.py
├── images/
├── .gitignore

## Run
Execute
``` Powershell
docker compose up -d
```
Rebuild
``` Powershell
docker compose up --build -d
```
## TODO
- Add .env

## Images
![Installation](images/installation.png)
![Docker](images/docker.png)
![Postgres](images/postgres.png)

## Technical
``` Powershell
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres-docker-basic-db-1
```
Should give you 172.18.0.2