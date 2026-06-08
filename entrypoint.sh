#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! nc -z postgres 5432; do
    sleep 1
done

echo "PostgreSQL started"

python manage.py migrate

exec "$@"
