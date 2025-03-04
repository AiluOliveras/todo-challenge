#!/bin/bash
echo "Creando migraciones"
python manage.py makemigrations

echo "Aplicando migraciones"
python manage.py migrate

echo "Iniciando server"
python manage.py runserver 0.0.0.0:8000