from django.urls import path
from .views import LizenzCreateView

urlpatterns = [
    path('license/create/', LizenzCreateView.as_view(), name='license-create'),
]