#!/usr/bin/env bash

pip install --upgrade pip

pip-review --local --auto

pip freeze > requirements.txt

#yarn upgrade --latest

./collectstatic.sh

