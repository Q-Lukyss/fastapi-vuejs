# Projet FastAPI, Mysql, Vuejs-Vite

## Requirements

Docker / [Docker-Desktop](https://www.docker.com/get-started/)

## Application

Cette Application est un template pour créer un Backend FastAPI en python couplé à un Frontend Vuejs.
Nginx est déja inclu dans le compose docker mais est pour l'instant commenté.

```
  # nginx:
  #   image: nginx:latest
  #   ports:
  #     - "8100:80"
  #   volumes:
  #     - ./nginx/nginx.conf:/etc/nginx/nginx.conf
  #   depends_on:
  #     - backend
  #     - frontend
```

### Débuter

Lancer Docker ou Docker Desktop

Mettez vous à la Racine du projet et exectuez

```
docker compose up --build
```

Une fois les images construites et les containers crées, tout est pret !

* Backend : http://localhost:8200/
* Frontend : http://localhost:8300/

Vous pouvez commencer votre développement et les changements se refleteront immédiatement sans devoir relancer les containers

