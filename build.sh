#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py shell -c "
from django.contrib.auth import get_user_model
import os
User = get_user_model()
u, created = User.objects.get_or_create(username='siteadmin', defaults={'email':'admin@example.com'})
u.set_password(os.environ['DJANGO_SUPERUSER_PASSWORD'])
u.is_staff = True
u.is_superuser = True
u.save()
print('OK:', 'created' if created else 'updated', u.username)
"
