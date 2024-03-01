# Utiliser une image de Python en tant que base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY ./requirements.txt /app/requirements.txt

# Copier tous les fichiers du backend dans le conteneur
COPY ./app /app

RUN apt-get update \
    && apt-get install -y build-essential libmariadb-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt


