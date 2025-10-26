# 🚀 Guide de Déploiement AWS

Ce guide vous explique étape par étape comment déployer votre application Django sur AWS Elastic Beanstalk.

## 📋 Table des matières

1. [Prérequis](#prérequis)
2. [Configuration AWS](#configuration-aws)
3. [Configuration GitHub](#configuration-github)
4. [Premier Déploiement](#premier-déploiement)
5. [Dépannage](#dépannage)

---

## Prérequis

- ✅ Compte AWS avec accès à Elastic Beanstalk
- ✅ Projet Django fonctionnel localement
- ✅ Compte GitHub
- ✅ Git installé

---

## Configuration AWS

### Étape 1 : Créer une application Elastic Beanstalk

1. Connectez-vous à la console AWS
2. Allez dans **Elastic Beanstalk**
3. Cliquez sur **Create Application**
4. Remplissez les informations :
   - **Application name** : `concours-esatic` (ou votre nom)
   - **Platform** : Python
   - **Platform branch** : Python 3.11 running on 64bit Amazon Linux 2
   - **Platform version** : Latest
5. Cliquez sur **Create application**

### Étape 2 : Créer un utilisateur IAM pour le déploiement

1. Allez dans **IAM** → **Users** → **Create user**
2. Nommez l'utilisateur : `github-actions-deploy`
3. Sélectionnez **Programmatic access**
4. Attachez la politique : `AWSElasticBeanstalkFullAccess`
5. **IMPORTANT** : Sauvegardez les clés d'accès :
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`

### Étape 3 : Configurer les variables d'environnement

1. Dans votre environnement Elastic Beanstalk
2. Allez dans **Configuration** → **Software**
3. Ajoutez ces variables d'environnement :
   ```
   DEBUG=False
   SECRET_KEY=votre-cle-secrete-ici
   ```
4. Cliquez sur **Apply**

---

## Configuration GitHub

### Étape 1 : Configurer les secrets GitHub

1. Allez sur votre dépôt GitHub
2. **Settings** → **Secrets and variables** → **Actions**
3. Cliquez sur **New repository secret**
4. Ajoutez ces secrets :

| Nom du secret | Valeur |
|---------------|--------|
| `AWS_ACCESS_KEY_ID` | Votre clé d'accès AWS |
| `AWS_SECRET_ACCESS_KEY` | Votre clé secrète AWS |
| `EB_APP_NAME` | `concours-esatic` |
| `EB_ENV_NAME` | Le nom de votre environnement EB |
| `AWS_REGION` | `eu-west-1` (ou votre région) |
| `SECRET_KEY` | Votre clé secrète Django |
| `DEBUG` | `False` |

### Étape 2 : Pousser votre code

```bash
git add .
git commit -m "Setup CI/CD pipeline"
git push origin main
```

Le pipeline se déclenchera automatiquement !

---

## Premier Déploiement

### Étapes du Pipeline

1. **Checkout** : Récupération du code
2. **Setup Python** : Installation de Python 3.11
3. **Install dependencies** : Installation des packages
4. **Run migrations** : Vérification des migrations
5. **Collect static** : Collecte des fichiers statiques
6. **Run tests** : Exécution des tests
7. **Deploy** : Déploiement sur AWS

### Vérifier le déploiement

1. Allez dans **GitHub Actions** → Voir les runs
2. Attendez que le pipeline se termine (≈ 5-10 minutes)
3. Récupérez l'URL depuis AWS Elastic Beanstalk
4. Visitez l'URL pour tester l'application

---

## Dépannage

### ❌ Le pipeline échoue à l'étape "Deploy"

**Cause** : Secrets manquants ou incorrects

**Solution** :
1. Vérifiez que tous les secrets sont configurés dans GitHub
2. Vérifiez que l'environnement EB existe
3. Vérifiez les permissions IAM

### ❌ Erreur 500 sur l'application

**Cause** : Variables d'environnement manquantes

**Solution** :
1. Vérifiez que `DEBUG=False` est configuré sur AWS
2. Vérifiez que `SECRET_KEY` est défini
3. Consultez les logs : **AWS EB** → **Logs** → **Request logs**

### ❌ Les fichiers statiques ne se chargent pas

**Cause** : Problème avec WhiteNoise ou collectstatic

**Solution** :
1. Vérifiez que `collectstatic` s'exécute dans le pipeline
2. Vérifiez la configuration WhiteNoise dans `settings.py`
3. Redéployez l'application

### ❌ Erreur de migration de base de données

**Cause** : Problèmes avec SQLite en production

**Solution** :
1. Passez à PostgreSQL ou MySQL
2. Configurez la base de données dans AWS RDS
3. Mettez à jour `DATABASES` dans `settings.py`

---

## Commandes utiles

### Logs du pipeline GitHub

```bash
# Cliquez sur "Actions" dans GitHub pour voir les logs
```

### Logs AWS Elastic Beanstalk

1. Console AWS → Elastic Beanstalk
2. Sélectionnez votre environnement
3. **Logs** → **Request logs**

### Déploiement manuel

```bash
# Activer l'environnement virtuel
newenv\Scripts\activate

# Créer le package de déploiement
eb deploy
```

---

## Prochaines étapes

- ✅ Configurer un domaine personnalisé
- ✅ Ajouter une base de données PostgreSQL
- ✅ Configurer le SSL/HTTPS
- ✅ Mettre en place la sauvegarde automatique
- ✅ Configurer le monitoring avec CloudWatch

---

## Support

Si vous rencontrez des problèmes :

1. Consultez les logs dans GitHub Actions
2. Consultez les logs AWS Elastic Beanstalk
3. Vérifiez la documentation Django deployment
4. Vérifiez la documentation AWS EB

**Bon déploiement ! 🚀**
