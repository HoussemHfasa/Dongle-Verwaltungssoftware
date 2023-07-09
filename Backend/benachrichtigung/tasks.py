from celery import shared_task
from .utils import check_lizenzen_ablauf

# Celery-Aufgabe zur Überprüfung des Ablaufs von Lizenzen
@shared_task
def check_lizenzen_ablauf_task():
    check_lizenzen_ablauf()