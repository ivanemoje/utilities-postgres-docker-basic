# Configuración de un contenedor PostgreSQL con Docker
PostgreSQL es un potente sistema de gestión de bases de datos relacionales de código abierto. En este repositorio, vamos a caminar a través del proceso de spinning hasta un contenedor PostgreSQL utilizando Docker.

También configuraremos una estructura básica de proyecto Python para interactuar con la base de datos.

## Pre-requisitos
- [Docker](https://www.docker.com/)

## Estructura del Proyecto
Primero, vamos a configurar la estructura de nuestro proyecto. Crea un nuevo directorio para tu proyecto y añade los siguientes archivos:

```markdown
postgres-docker/
│
├── .gitignore
├── Dockerfile
├── main.py
├── requirements.txt
└── database.py
├── images/
├── .gitignore
```

## Ejecutar
Ejecutar
``` Powershell
docker compose up -d
```
Reconstruir
Powershell
docker compose up --build -d
```
## TODO
- Añadir .env

## Técnica
``` Powershell
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres-docker-basic-db-1
```
Debería darte 172.18.0.2