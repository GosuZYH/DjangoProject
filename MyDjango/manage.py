#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from MyDjango.utils.log import Logger


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyDjango.settings')
    try:
        from django.core.management import execute_from_command_line
        Logger(level="debug").log.debug("Start django server...")
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    if len(sys.argv) > 1:
        execute_from_command_line(sys.argv)
    else:
        execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])


if __name__ == '__main__':
    main()
