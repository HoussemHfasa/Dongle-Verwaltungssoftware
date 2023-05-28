"""Befehlszeilen-Tool von Django für administrative Aufgaben."""

import os  
import sys

def main():
    """Administrative Aufgaben ausführen."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django konnte nicht importiert werden. Sind Sie sicher, dass es installiert ist und "
            "auf der PYTHONPATH-Umgebungsvariable verfügbar ist? Haben Sie "
            "vergessen, eine virtuelle Umgebung zu aktivieren?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()