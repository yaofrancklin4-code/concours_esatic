# Concours ESATIC - Projet Django

Ce projet est une application Django simple pour le concours ESATIC, développée avec Django 5.2.7.

## Description

L'application "Mon_appli" comprend trois pages principales :
- **Accueil** : Page d'accueil du site
- **Inscription** : Formulaire d'inscription
- **Contact** : Page de contact

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/yaofrancklin4-code/concours_esatic.git
   cd concours_esatic
   ```

2. Créez un environnement virtuel :
   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows : env\Scripts\activate
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Appliquez les migrations :
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Collectez les fichiers statiques :
   ```bash
   python manage.py collectstatic
   ```

6. Lancez le serveur de développement :
   ```bash
   python manage.py runserver
   ```

L'application sera accessible à l'adresse http://127.0.0.1:8000/

## Déploiement

Le projet utilise un pipeline CI/CD GitHub Actions pour le déploiement automatique sur AWS Elastic Beanstalk.

### Prérequis pour le déploiement

1. Créez une application Elastic Beanstalk sur AWS.
2. Configurez les secrets suivants dans les paramètres de votre dépôt GitHub :
   - `AWS_ACCESS_KEY_ID` : Votre clé d'accès AWS
   - `AWS_SECRET_ACCESS_KEY` : Votre clé secrète AWS
   - `EB_APP_NAME` : Nom de votre application Elastic Beanstalk
   - `EB_ENV_NAME` : Nom de l'environnement Elastic Beanstalk

### Pipeline CI/CD

Le pipeline effectue les étapes suivantes :
- **Build** : Installation des dépendances, migrations Django, collecte des fichiers statiques, exécution des tests
- **Deploy** : Déploiement sur AWS Elastic Beanstalk

## Structure du projet

```
Test/
├── Mon_appli/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── Test/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

## Technologies utilisées

- **Django** 5.2.7
- **Python** 3.11
- **AWS Elastic Beanstalk** pour le déploiement
- **GitHub Actions** pour le CI/CD

## Auteur

[yaofrancklin4-code](https://github.com/yaofrancklin4-code)
