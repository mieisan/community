#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

DJANGO_SUPERUSER_PASSWORD="$DJANGO_SUPERUSER_PASSWORD" python manage.py createsuperuser --noinput --username admin --email admin@example.com || true
