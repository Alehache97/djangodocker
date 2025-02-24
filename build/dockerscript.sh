#!/bin/bash
cd /usr/share/app/
export DJANGO_SUPERUSER_PASSWORD=$DJANGO_PASSWORD
sleep 20
sed -i "s/^ALLOWED_HOSTS = .*$/ALLOWED_HOSTS = ['$ALLOWED_HOSTS']/" /usr/share/app/django_publicaciones/settings.py
python3 manage.py migrate
python manage.py createsuperuser --username=$DJANGO_USER --email=$DJANGO_EMAIL --noinput
python3 manage.py runserver 0.0.0.0:8084

