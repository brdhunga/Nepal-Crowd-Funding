#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals

import os
import sys

import environ
env = environ.Env()
environ.Env.read_env()

try:
    DJANGO_SETTINGS_MODULE = env('DJANGO_SETTINGS_MODULE')
except KeyError:
    print("****\n" * 3)
    print("Warning !!!, make sure to change settings in production")
    print("****\n" * 3)
    DJANGO_SETTINGS_MODULE = "wagtail_crowd_funding.settings.dev"


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)