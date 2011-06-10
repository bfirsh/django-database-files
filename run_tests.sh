#!/bin/sh
PYTHONPATH=. DJANGO_SETTINGS_MODULE="database_files.tests.settings" django-admin.py test tests

