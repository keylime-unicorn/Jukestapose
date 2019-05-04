#!/bin/sh

mkdir -p ./Music
FLASK_APP=webserver.py flask run --host=0.0.0.0
