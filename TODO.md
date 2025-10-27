# TODO - Pipeline CI/CD AWS

## ✅ Terminé
- [x] Analyser la configuration existante du pipeline
- [x] Vérifier les fichiers de déploiement (workflow, EB config, Procfile, Dockerfile)
- [x] Confirmer que tous les composants sont présents

## 🔄 En cours
- [ ] Créer un utilisateur IAM AWS pour le déploiement
- [ ] Configurer les secrets GitHub (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, EB_APP_NAME, EB_ENV_NAME, AWS_REGION, SECRET_KEY)
- [ ] Tester le pipeline en poussant sur main
- [ ] Vérifier le déploiement sur AWS Elastic Beanstalk

## 📋 Instructions pour l'utilisateur

### 1. Créer un utilisateur IAM AWS
1. Aller dans la console AWS → IAM → Users → Create user
2. Nom : `github-actions-deploy`
3. Type d'accès : Programmatic access
4. Politique : `AWSElasticBeanstalkFullAccess`
5. Sauvegarder les clés :
   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY

### 2. Configurer les secrets GitHub
Aller dans votre dépôt GitHub → Settings → Secrets and variables → Actions → New repository secret

Ajouter ces secrets :
- `AWS_ACCESS_KEY_ID` : [votre clé d'accès]
- `AWS_SECRET_ACCESS_KEY` : [votre clé secrète]
- `EB_APP_NAME` : concours-esatic
- `EB_ENV_NAME` : concours-esatic-env
- `AWS_REGION` : eu-west-1
- `SECRET_KEY` : [générez une clé secrète Django]

### 3. Tester le déploiement
```bash
git add .
git commit -m "Setup CI/CD pipeline"
git push origin main
```

### 4. Vérifier
- Aller dans GitHub Actions pour voir le pipeline
- Attendre 5-10 minutes
- Récupérer l'URL depuis AWS Elastic Beanstalk
- Tester l'application déployée

## 🔧 Dépannage
- Vérifier que tous les secrets sont configurés
- S'assurer que l'environnement EB existe
- Consulter les logs GitHub Actions et AWS EB en cas d'erreur
