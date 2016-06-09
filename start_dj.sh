#!/bin/bash
source /usr/local/bin/virtualenvwrapper.sh
workon djangotest1
nohup python manage.py runserver &

