#!/usr/bin/env bash
set -euxo pipefail

pip install --upgrade pip
pip install -r requirements.txt

./manage.py collectstatic --no-input
./manage.py migrate
./manage.py check

