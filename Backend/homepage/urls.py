from django.urls import path
from .views import DongleView

urlpatterns = [
    path('homepage/', DongleView.as_view()),
]