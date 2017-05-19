#!/bin/bash

sudo pip install virtualenv
virtualenv src/venv
source src/venv/bin/activate
pip install -r src/requirements.txt
deactivate
