#! /usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

python manage.py migrate
python manage.py runserver 0.0.0.0:8000