# 🚀 Guide de Déploiement EC2 SSH

Ce guide vous explique étape par étape comment déployer votre application Django sur AWS EC2 via SSH depuis GitHub Actions.

## 📋 Table des matières

1. [Prérequis](#prérequis)
2. [Configuration AWS](#configuration-aws)
3. [Configuration GitHub](#configuration-github)
4. [Premier Déploiement](#premier-déploiement)
5. [Dépannage](#dépannage)

---

## Prérequis

- ✅ Compte AWS avec accès à EC2
- ✅ Projet Django fonctionnel localement
- ✅ Compte GitHub
- ✅ Git installé

---

## Configuration AWS EC2

### Étape 1 : Lancer une instance EC2

1. Connectez-vous à la console AWS
2. Allez dans **EC2** → **Instances**
3. Cliquez sur **Launch Instance**
4. Choisissez **Ubuntu Server 22.04 LTS** (ou plus récent)
5. Sélectionnez un type d'instance : `t2.micro` (gratuit)
6. Configurez le stockage : 8GB minimum
7. **Security Group** : Ajoutez les règles :
   - SSH (port 22) : `0.0.0.0/0` (temporaire, restreignez plus tard)
   - HTTP (port 80) : `0.0.0.0/0`
   - Custom TCP (port 8000) : `0.0.0.0/0` (pour gunicorn)
8. Lancez l'instance

### Étape 2 : Configuration initiale de l'EC2

Connectez-vous en SSH à votre instance :

```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

Installez les dépendances de base :

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv nginx
```

Créez l'environnement virtuel :

```bash
python3 -m venv /home/ubuntu/venv
```

Créez le répertoire du projet :

```bash
mkdir /home/ubuntu/django-app
```

### Étape 3 : Générer une clé SSH pour GitHub Actions

Sur votre machine locale :

```bash
ssh-keygen -t rsa -b 4096 -C "github-actions" -f ~/.ssh/github_actions
```

Ajoutez la clé publique à `~/.ssh/authorized_keys` sur l'EC2 :

```bash
cat ~/.ssh/github_actions.pub | ssh -i your-ec2-key.pem ubuntu@your-ec2-ip "cat >> ~/.ssh/authorized_keys"
```

La clé privée sera utilisée dans les secrets GitHub.

---

## Configuration GitHub

### Étape 1 : Configurer les secrets GitHub

1. Allez sur votre dépôt GitHub
2. **Settings** → **Secrets and variables** → **Actions**
3. Cliquez sur **New repository secret**
4. Ajoutez ces secrets :

| Nom du secret | Valeur |
|---------------|--------|
| `SSH_HOST` | IP publique de votre EC2 |
| `SSH_USER` | `ubuntu` |
| `SSH_KEY` | Contenu de `~/.ssh/github_actions` (clé privée) |
| `EC2_IP` | IP publique de votre EC2 (pour ALLOWED_HOSTS) |
| `SECRET_KEY` | Votre clé secrète Django |
| `DEBUG` | `False` |

### Étape 2 : Pousser votre code

```bash
git add .
git commit -m "Switch to EC2 SSH deployment"
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
7. **SSH Setup** : Configuration du service systemd
8. **File Sync** : Synchronisation des fichiers via SCP
9. **Deploy** : Exécution du script de déploiement

### Vérifier le déploiement

1. Allez dans **GitHub Actions** → Voir les runs
2. Attendez que le pipeline se termine (≈ 3-5 minutes)
3. Visitez `http://your-ec2-ip:8000` pour tester l'application

---

## Dépannage

### ❌ Le pipeline échoue à l'étape SSH

**Cause** : Problèmes de connexion SSH

**Solution** :
1. Vérifiez que l'IP EC2 est correcte dans `SSH_HOST`
2. Vérifiez que la clé SSH est correctement formatée (pas d'espaces en trop)
3. Vérifiez les permissions du Security Group (port 22 ouvert)
4. Testez la connexion SSH manuellement

### ❌ Erreur 500 sur l'application

**Cause** : Variables d'environnement manquantes

**Solution** :
1. Vérifiez que `DEBUG=False` et `SECRET_KEY` sont définis
2. Vérifiez que `EC2_IP` est dans `ALLOWED_HOSTS`
3. Consultez les logs gunicorn : `sudo journalctl -u gunicorn`

### ❌ Les fichiers statiques ne se chargent pas

**Cause** : Problème avec WhiteNoise ou collectstatic

**Solution** :
1. Vérifiez que `collectstatic` s'exécute dans le script deploy.sh
2. Vérifiez la configuration WhiteNoise dans `settings.py`
3. Redéployez l'application

### ❌ Gunicorn ne démarre pas

**Cause** : Problème avec le service systemd

**Solution** :
1. Vérifiez le statut : `sudo systemctl status gunicorn`
2. Consultez les logs : `sudo journalctl -u gunicorn`
3. Vérifiez que le virtualenv existe : `/home/ubuntu/venv`
4. Redémarrez manuellement : `sudo systemctl restart gunicorn`

---

## Commandes utiles

### Logs du pipeline GitHub

```bash
# Cliquez sur "Actions" dans GitHub pour voir les logs
```

### Logs Gunicorn sur EC2

```bash
sudo journalctl -u gunicorn -f
```

### Status du service

```bash
sudo systemctl status gunicorn
sudo systemctl restart gunicorn
```

### Déploiement manuel

```bash
# Sur l'EC2
cd /home/ubuntu/django-app
source /home/ubuntu/venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart gunicorn
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
2. Consultez les logs gunicorn sur EC2
3. Vérifiez la documentation Django deployment
4. Vérifiez la documentation AWS EC2

**Bon déploiement ! 🚀**
