# Guide de Déploiement CI/CD - AWS Elastic Beanstalk

## 🚀 Configuration des Secrets GitHub

Dans votre dépôt GitHub, allez dans **Settings → Secrets and variables → Actions** et ajoutez :

### Secrets requis :

| Secret | Description | Exemple |
|--------|-------------|---------|
| `AWS_ACCESS_KEY_ID` | Clé d'accès AWS IAM | `AKIAIOSFODNN7EXAMPLE` |
| `AWS_SECRET_ACCESS_KEY` | Clé secrète AWS IAM | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |
| `EB_APP_NAME` | Nom de l'application Elastic Beanstalk | `concours-esatic` |
| `EB_ENV_NAME` | Nom de l'environnement | `concours-esatic-env` |
| `AWS_REGION` | Région AWS | `eu-west-1` |

## 📋 Étapes de Configuration AWS

### 1. Créer une application Elastic Beanstalk

```bash
# Via AWS CLI (optionnel)
eb init --platform python-3.11 --region eu-west-1
eb create concours-esatic-env
```

### 2. Configurer les variables d'environnement sur AWS

Dans Elastic Beanstalk → Configuration → Software, ajoutez :
- `DEBUG=False`
- `SECRET_KEY=votre-cle-secrete-django`

### 3. Permissions IAM requises

Votre utilisateur IAM doit avoir les permissions :
- `AWSElasticBeanstalkFullAccess`
- `IAMReadOnlyAccess`

## 🔄 Processus de Déploiement

Le pipeline se déclenche automatiquement sur push vers `main` :

1. **Build** : Installation des dépendances
2. **Tests** : Exécution des tests Django
3. **Collecte** : Collecte des fichiers statiques
4. **Package** : Création du package de déploiement
5. **Deploy** : Déploiement sur AWS Elastic Beanstalk

## 🌐 Accès à l'application

Une fois déployée : `http://votre-environnement.region.elasticbeanstalk.com`

## 🐛 Dépannage

### Pipeline échoue
- Vérifiez les secrets GitHub
- Vérifiez que l'environnement EB existe
- Consultez les logs dans Actions

### Erreurs de déploiement
- Vérifiez les logs Elastic Beanstalk
- Vérifiez les variables d'environnement AWS