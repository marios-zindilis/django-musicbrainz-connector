#!/usr/bin/env python

# This minimal `manage.py` script can be used to create migrations.

import sys

import django
from django.conf import settings
from django.core.management import execute_from_command_line

settings.configure(INSTALLED_APPS=["django_musicbrainz_connector"])
django.setup()
execute_from_command_line(sys.argv)
