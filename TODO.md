# TODO: Fix and Relaunch CI/CD Pipeline for AWS

## Steps to Complete
- [x] Update .github/workflows/ci-cd.yml to include missing Django steps (makemigrations, migrate, collectstatic) and add AWS Elastic Beanstalk deployment.
- [ ] Ensure AWS credentials are set as GitHub secrets (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, EB_APP_NAME, EB_ENV_NAME).
- [ ] Commit and push changes to trigger the pipeline.
- [ ] Monitor GitHub Actions for successful build and deployment.
- [ ] Test the deployed app on AWS.
