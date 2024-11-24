# Setting Up a PostgreSQL Container with Docker and Connecting to a Client
PostgreSQL is a powerful, open-source relational database management system. In this repository, we'll walk through the process of spinning up a PostgreSQL container using Docker and connecting it to a client like DBeaver or pgAdmin. 

We'll also set up a basic Python project structure to interact with the database.

## Pre-requisites
- [Docker](https://www.docker.com/)
- [Docker Windows](https://www.docker.com/)
- [PgAdmin](https://www.pgadmin.org/) or [DBeaver](https://dbeaver.io/)

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