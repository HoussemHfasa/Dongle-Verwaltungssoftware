#apps.py
from django.apps import AppConfig

class UserLogginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'User_loggin'

    def ready(self):
        import User_loggin.signals