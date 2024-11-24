# Configurer un conteneur PostgreSQL avec Docker
PostgreSQL est un puissant système de gestion de base de données relationnelle open-source. Dans ce dépôt, nous allons suivre le processus de création d'un conteneur PostgreSQL à l'aide de Docker.

Nous mettrons également en place une structure de projet Python de base pour interagir avec la base de données.

## Pré-requis
- [Docker](https://www.docker.com/)

## Structure du projet
Tout d'abord, mettons en place la structure de notre projet. Créez un nouveau répertoire pour votre projet et ajoutez les fichiers suivants :

postgres-docker/
│
├── .gitignore
├── Dockerfile
├── main.py
├── requirements.txt
└── database.py
├── images/
├─── .gitignore

## Exécuter
Exécuter
``` Powershell
docker compose up -d
```
Reconstruire
``` Powershell
docker compose up --build -d
```
## TODO
- Ajouter .env

## Technique
```` Powershell
docker inspect -f '{{range .NetworkSettings.Networks}}{{{.IPAddress}}{{{end}}' postgres-docker-basic-db-1
```