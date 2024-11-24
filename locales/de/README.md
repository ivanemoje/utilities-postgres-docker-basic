# Einrichten eines PostgreSQL-Containers mit Docker
PostgreSQL ist ein leistungsfähiges, quelloffenes relationales Datenbankmanagementsystem. In diesem Repository werden wir den Prozess des Aufsetzens eines PostgreSQL-Containers mit Docker durchlaufen.

Wir werden auch eine grundlegende Python-Projektstruktur für die Interaktion mit der Datenbank einrichten.

## Voraussetzungen
- [Docker](https://www.docker.com/)

## Projektstruktur
Lassen Sie uns zunächst unsere Projektstruktur einrichten. Erstellen Sie ein neues Verzeichnis für Ihr Projekt und fügen Sie die folgenden Dateien hinzu:

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

## Ausführen
Ausführen
```` Powershell
docker compose up -d
```
Neu erstellen
Powershell ausführen
docker compose up --build -d
```
## TODO
- .env hinzufügen

## Technisch
```` Powershell
docker inspect -f '{{bereich .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres-docker-basic-db-1
```
Sollte Ihnen 172.18.0.2 liefern