


# Développement d'une API via Django REST/ Back-end PostSQL 

## Overview

Epic Events est une entreprise de conseil et de gestion dans l'événementiel qui répond 
aux besoins des start-up voulant organiser des « fêtes épiques ». Ce projet vise à aider cette entreprise via la 
création d'un nouveau CRM avec Django administration en front-end. 


L'application Django fournit un ensemble d’endpoints sécurisés pour l’API à l'aide du framework Django REST (avec une base de 
données PostgreSQL) pour permettre les opérations CRUD (créer, lire, mettre à jour et supprimer) 
appliquées aux divers objets CRM. Un diagramme de classes a été réalisé sous l'approche « domain-driven design » et en 
respectant les exigences fonctionelles et techniques du client.

L'ensemble des Endpoints ont été testés via POSTMAN (tant pour les fonctionnalités que pour la sécurité). Le projet a notamment pour objectif d'appliquer 
différents rôles et permissions au niveau des utilisateurs/employés (service de vente, service de support, service admin ...)

**API permet notamment de :**
* Créer divers clients(prospect ou non)/contrats/événements/employés
* D'ajouter un employé à un événement spécifique en fonction des permissions du service
* de créer automatique un événement lors de la signature d'un contrat 
* Rechercher par filtres

L'Authentification des employés est réalisée via JWT (JSON Web Token)- L'Authentification est obligatoire.



## Test et developpement

1. Pré-requis pour l'utilisation de API:

    * Installer la dernière version de Python sur le site - https://www.python.org
    * Ouvrir l'interpréteur de commandes de Python
    * Créer un nouveau repertoire via la commande : ```cd mkdir projet12```
    * Initialiser un environnement virtuel via la commande : ```python -m venv env```
    * Taper dans la console et au niveau du dossier racine : ```git init```
    * Cloner le dépo via la console : ```git clone https://github.com/JulienC-Dev/P12_API_EPIC_EVENT_POSTGRES/blob/develop/epic/myapp/models.py```
    * Puis installer les dépendances: ```pip install -r requirements.txt```
    * Télécharger Postman en local à l'adresse suivante pour la gestion des requêtes: ```https://www.postman.com/downloads/```

2. Connection au serveur local http://127.0.0.1:8000/
   * Aller sur le sous-dossier - Projet10 via la commande  : ```cd Projet12```
   * Créer un superuser via la ligne de commande ou utiliser les dataset de connection : ```python manage.py createsuperuser```
   * Lancer le serveur local via la commande : ```python manage.py runserver```
   * Ouvrir le naviguateur web puis taper dans la barre de recherche : ```http://127.0.0.1:8000/admin/```

## Dataset de connection

La base de données est en postSQL.

1. Connection au site admin local http://127.0.0.1:8000/admin

| Nom Admin          | Mots de passe |
| -------------      |:-------------:|
| julien             | julien        |


## Ressources

Vous pouvez trouver ces ressources utiles:

* Overview Django : https://www.djangoproject.com/start/overview/
* Overview Django REST : https://www.django-rest-framework.org
* Overview Postman : https://learning.postman.com/docs/getting-started/introduction/

## Version 0.1.0

Auteur JulienC-Dev - github : https://github.com/JulienC-Dev/P12_API_EPIC_EVENT_POSTGRES/blob/develop/epic/myapp/models.py

