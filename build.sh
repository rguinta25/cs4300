#!/usr/bin/env bash
set -o errexit

cd homework2
<<<<<<< HEAD

=======
>>>>>>> 7a9ac5d (render)
pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate
