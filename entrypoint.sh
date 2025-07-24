#!/bin/sh

# Run migrations
python manage.py migrate

# Create superuser automatically if not exists with environment variables
python manage.py shell << END
import os
from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

if username and password and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email or "", password=password)
END

exec "$@"