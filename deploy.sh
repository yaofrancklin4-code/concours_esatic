#!/bin/bash

# Deploy script for Django app on EC2
# This script assumes:
# - Ubuntu EC2 instance
# - Python 3.11 installed
# - virtualenv installed
# - Project directory: /home/ubuntu/django-app
# - Virtual environment: /home/ubuntu/venv

set -e

echo "Starting deployment..."

# Variables
PROJECT_DIR="/home/ubuntu/django-app"
VENV_DIR="/home/ubuntu/venv"
USER="ubuntu"

# Activate virtual environment
source $VENV_DIR/bin/activate

# Navigate to project directory
cd $PROJECT_DIR

# Install/update dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Restart gunicorn service
sudo systemctl restart gunicorn

# Reload nginx if using it
# sudo nginx -t && sudo nginx -s reload

echo "Deployment completed successfully!"
