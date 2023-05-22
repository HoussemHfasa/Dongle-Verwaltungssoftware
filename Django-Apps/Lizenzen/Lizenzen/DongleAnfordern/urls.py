from django.urls import path
from . import views
from django.urls import path
from .views import create_ticket

urlpatterns = [
    path('api/create_ticket/', create_ticket, name='create_ticket'),
    # ... andere URLs in Ihrem Django-Projekt
]