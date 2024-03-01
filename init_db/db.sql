-- https://www.mocodo.net/?mcd=eNpdTkEOgzAMu_cVeUAv7MiNw7QL2hdQVSwUqbRVaHn_ShjTxCV2FMf2UAuq9MTz5JRaimm1lAWKBl5YYKl70_AVdA8aeRcYnX17DQexVLgc4GIEpi1JYRjvCpYkvEHUZDyljb0Qm4dOzV8OpvHGPNcsNWq1dsFvu7Xz2dLOIcBcknvInxHNrcrl9QGEoFZK

DROP DATABASE IF EXISTS `cyka`;
CREATE DATABASE `cyka`;
USE `cyka`;

CREATE TABLE Auteur (
  PRIMARY KEY (id_auteur),
  id_auteur INTEGER NOT NULL AUTO_INCREMENT,
  nom       VARCHAR(42),
  prenom    VARCHAR(42)
);

CREATE TABLE categoriser (
  PRIMARY KEY (id_livre, id_genre),
  id_livre INTEGER NOT NULL,
  id_genre INTEGER NOT NULL
);

CREATE TABLE ecrire (
  PRIMARY KEY (id_auteur, id_livre),
  id_auteur INTEGER NOT NULL,
  id_livre  INTEGER NOT NULL
);

CREATE TABLE emprunter (
  PRIMARY KEY (id_livre, id_emprunteur),
  id_livre      INTEGER NOT NULL AUTO_INCREMENT,
  id_emprunteur INTEGER NOT NULL,
  date_emprunt  VARCHAR(42)
);

CREATE TABLE Emprunteur (
  PRIMARY KEY (id_emprunteur),
  id_emprunteur INTEGER NOT NULL AUTO_INCREMENT,
  nom           VARCHAR(42),
  prenom        VARCHAR(42),
  cp            VARCHAR(42),
  ville         VARCHAR(42)
);

CREATE TABLE Genre (
  PRIMARY KEY (id_genre),
  id_genre INTEGER NOT NULL AUTO_INCREMENT,
  nom      VARCHAR(42)
);

CREATE TABLE Livre (
  PRIMARY KEY (id_livre),
  id_livre     INTEGER NOT NULL AUTO_INCREMENT,
  titre        VARCHAR(42),
  annee_sortie VARCHAR(42)
);

ALTER TABLE categoriser ADD FOREIGN KEY (id_genre) REFERENCES Genre (id_genre);
ALTER TABLE categoriser ADD FOREIGN KEY (id_livre) REFERENCES Livre (id_livre);

ALTER TABLE ecrire ADD FOREIGN KEY (id_livre) REFERENCES Livre (id_livre);
ALTER TABLE ecrire ADD FOREIGN KEY (id_auteur) REFERENCES Auteur (id_auteur);

ALTER TABLE emprunter ADD FOREIGN KEY (id_emprunteur) REFERENCES Emprunteur (id_emprunteur);
ALTER TABLE emprunter ADD FOREIGN KEY (id_livre) REFERENCES Livre (id_livre);

-- Insertion des auteurs
INSERT INTO Auteur (id_auteur, nom, prenom) VALUES
(1, 'Rowling', 'J.K.'),
(2, 'Martin', 'George R.R.'),
(3, 'Murakami', 'Haruki');

-- Insertion des livres
INSERT INTO Livre (id_livre, titre, annee_sortie) VALUES
(1, 'Harry Potter à l\'école des sorciers', '1997'),
(2, 'Le Trône de Fer', '1996'),
(3, '1Q84', '2009');

-- Insertion des relations entre auteurs et livres
INSERT INTO ecrire (id_auteur, id_livre) VALUES
('1', '1'), -- J.K. Rowling a écrit "Harry Potter à l'école des sorciers"
('2', '2'), -- George R.R. Martin a écrit "Le Trône de Fer"
('3', '3'); -- Haruki Murakami a écrit "1Q84"