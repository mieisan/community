#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

python manage.py shell << 'EOF'
from django.contrib.auth import get_user_model
import os

User = get_user_model()
username = "siteadmin"
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
email = "admin@example.com"

user, created = User.objects.get_or_create(username=username, defaults={"email": email})
user.set_password(password)
user.is_staff = True
user.is_superuser = True
user.save()

print("created new user" if created else "updated existing user", username)
EOF
