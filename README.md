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
   python -m venv newenv
   source newenv/bin/activate  # Sur Windows : newenv\Scripts\activate
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

## Déploiement sur AWS

Le projet utilise un **pipeline CI/CD automatisé** avec GitHub Actions pour le déploiement sur AWS Elastic Beanstalk.

### 🚀 Architecture du Pipeline CI/CD

Le pipeline est automatiquement déclenché à chaque push sur la branche `main` et effectue :

1. **Build** : Installation des dépendances
2. **Tests** : Exécution des tests Django
3. **Collecte** : Collecte des fichiers statiques
4. **Déploiement** : Déploiement automatique sur AWS Elastic Beanstalk

### 📋 Prérequis pour le déploiement

#### 1. Créer une application AWS Elastic Beanstalk

Sur AWS Console :
- Allez dans **Elastic Beanstalk**
- Créez une nouvelle application
- Choisissez la plateforme **Python 3.11**
- Nommez votre environnement (ex: `concours-esatic-env`)

#### 2. Configurer les secrets GitHub

Dans votre dépôt GitHub, allez dans :
**Settings → Secrets and variables → Actions**

Ajoutez ces secrets :

| Secret | Description | Exemple |
|--------|-------------|---------|
| `AWS_ACCESS_KEY_ID` | Clé d'accès AWS IAM | `AKIAIOSFODNN7EXAMPLE` |
| `AWS_SECRET_ACCESS_KEY` | Clé secrète AWS IAM | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
| `EB_APP_NAME` | Nom de l'app Elastic Beanstalk | `concours-esatic` |
| `EB_ENV_NAME` | Nom de l'environnement | `concours-esatic-env` |
| `AWS_REGION` | Région AWS (optionnel) | `eu-west-1` |
| `SECRET_KEY` | Clé secrète Django | `votre-cle-secrete` |
| `DEBUG` | Mode debug (True/False) | `False` |

#### 3. Configurer les variables d'environnement sur AWS

Dans Elastic Beanstalk → Configuration → Software :
- Ajoutez `DEBUG=False`
- Ajoutez `SECRET_KEY=votre-cle-secrete`

### 🔧 Configuration du Pipeline

Le fichier `.github/workflows/deploy-aws.yml` contient la configuration complète du pipeline :

```yaml
on:
  push:
    branches:
      - main  # Se déclenche sur push vers main
```

### 🧪 Test Local

```bash
python deploy_local.py
```

### 🌐 Accès à l'application

Une fois déployée, votre application sera accessible à l'URL :
```
http://votre-environnement.region.elasticbeanstalk.com
```

### 📦 Méthodes de déploiement

#### Option 1 : Elastic Beanstalk (Recommandé)
- ✅ Simple et rapide
- ✅ Gestion automatique du scaling
- ✅ Configuration via Procfile

#### Option 2 : Docker sur ECS
- Utilisez le fichier `Dockerfile` fourni
- Déployez sur AWS ECS ou EC2

#### Option 3 : Déploiement manuel
```bash
# Créer un fichier ZIP
zip -r deploy.zip . -x "*.git*" "venv/*" "*.pyc"

# Uploader via la console AWS EB
eb deploy
```

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
│       └── deploy.yml
├── .gitignore
├── Dockerfile
├── Procfile
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
- **Gunicorn** pour le serveur WSGI
- **WhiteNoise** pour les fichiers statiques

## 🔐 Sécurité

- ✅ `.gitignore` configuré pour exclure les secrets
- ✅ `DEBUG=False` en production
- ✅ Variables d'environnement pour les clés secrètes
- ✅ `ALLOWED_HOSTS` configuré pour AWS

## 🐛 Dépannage

### Le pipeline échoue
- Vérifiez que tous les secrets sont configurés
- Vérifiez que l'environnement EB existe
- Consultez les logs GitHub Actions

### Erreur 404 sur les fichiers statiques
- Vérifiez que `collectstatic` s'exécute dans le pipeline
- Vérifiez la configuration WhiteNoise

### Base de données
- SQLite pour le développement
- Utilisez PostgreSQL ou MySQL pour la production

## Auteur

[yaofrancklin4-code](https://github.com/yaofrancklin4-code)

## Licence

Ce projet est développé pour le concours ESATIC.
