from celery import shared_task
from .utils import check_lizenzen_ablauf


@shared_task
def check_lizenzen_ablauf_task():
    check_lizenzen_ablauf()