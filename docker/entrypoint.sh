#!/bin/bash

set -e
until nc -z $DB_HOST $DB_PORT; do
   echo "$(date) - Waiting for Database Connection..."
   sleep 1
done

echo "***--------------------------- Install Dependencies ---------------------------***"
pip3 install -r requirements.txt

if [[ $ENABLE_MIGRATIONS == "true" ]]; then
    echo "***--------------------------- Migrations ---------------------------***"
    python manage.py makemigrations
    python manage.py migrate
fi

echo "***--------------------------- Compile Static ---------------------------***"
python manage.py collectstatic --noinput

echo "***--------------------------- Run Server ---------------------------***"
if  [[ $RUN_MODE == "PROD" ]]; then
  gunicorn creditBank.wsgi:application -w $GUNICORN_WORKERS -b :8000;
else
  python manage.py runserver 0.0.0.0:8000;
fi
