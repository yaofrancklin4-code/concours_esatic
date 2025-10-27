# TODO - Pipeline CI/CD EC2 SSH Deployment

## ✅ Terminé
- [x] Analyser la configuration existante du pipeline
- [x] Vérifier les fichiers de déploiement (workflow, EB config, Procfile, Dockerfile)
- [x] Confirmer que tous les composants sont présents

## 🔄 En cours
- [ ] Update .github/workflows/deploy.yml to use SSH deployment
- [ ] Create deploy.sh script for EC2 setup and deployment
- [ ] Create gunicorn.service systemd file
- [ ] Update Test/settings.py ALLOWED_HOSTS for EC2
- [ ] Update DEPLOYMENT.md for EC2 guide
- [ ] Manual EC2 setup (Ubuntu, Python, virtualenv, nginx if needed)
- [ ] Configure SSH key in GitHub secrets
- [ ] Test the pipeline

## 📋 Instructions pour l'utilisateur

### 1. Setup EC2 Instance
1. Launch Ubuntu EC2 instance
2. Install Python 3.11, virtualenv, nginx
3. Create project directory: `/home/ubuntu/django-app`
4. Setup SSH key for GitHub Actions

### 2. Configure GitHub Secrets
Add these secrets to GitHub repository:
- `SSH_HOST`: EC2 public IP
- `SSH_USER`: ubuntu
- `SSH_KEY`: Private SSH key
- `EC2_IP`: EC2 public IP for ALLOWED_HOSTS

### 3. Test the deployment
```bash
git add .
git commit -m "Switch to EC2 SSH deployment"
git push origin main
```

### 4. Verify
- Check GitHub Actions logs
- SSH to EC2 and verify app is running
- Test the application at EC2 IP

## 🔧 Dépannage
- Verify SSH connection works
- Check EC2 security groups (ports 22, 80, 8000)
- Ensure virtualenv is activated in deploy.sh
- Check systemd service status
