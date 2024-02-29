# Utiliser une image Node.js comme base
FROM node:latest

# Créer et définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers package.json et package-lock.json pour installer les dépendances
COPY ./package*.json .

# Installer les dépendances
RUN npm install

# Copier le reste des fichiers de l'application
COPY . .

CMD [ "npm", "run", "dev" ]