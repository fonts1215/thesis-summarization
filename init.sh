#!/bin/bash
set -e

echo "Starting app ..."
# service ssh start

# python /code/manage.py runserver 0.0.0.0:8080
hypercorn main.py -b 0.0.0.0:8000

echo "END app ..."
