# TODO: Fix and Relaunch CI/CD Pipeline for AWS

## Steps to Complete
- [x] Update .github/workflows/ci-cd.yml to include missing Django steps (makemigrations, migrate, collectstatic) and add AWS Elastic Beanstalk deployment.
- [x] Add gunicorn to requirements.txt for production server.
- [x] Update Test/settings.py: Add STATIC_ROOT, make DEBUG and ALLOWED_HOSTS environment-dependent for production safety.
- [x] Add MEDIA_URL and MEDIA_ROOT to settings.py for media files.
- [x] Create .ebextensions/django.config for Elastic Beanstalk configuration.
- [x] Fix .ebextensions/django.config to include container commands for migrate and collectstatic.
- [x] Change DEBUG default to False and ALLOWED_HOSTS to ['*'] for production.
- [x] Update workflow to use EB CLI instead of action for better control.
- [ ] Ensure AWS credentials are set as GitHub secrets (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, EB_APP_NAME, EB_ENV_NAME).
- [x] Commit and push changes to trigger the pipeline.
- [ ] Monitor GitHub Actions for successful build and deployment.
- [ ] Test the deployed app on AWS.
