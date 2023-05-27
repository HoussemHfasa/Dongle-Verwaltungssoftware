
from django.urls import path
from .utils import check_lizenzen_ablauf  # Import view directly

urlpatterns = [
    path('benachrichtigung/', check_lizenzen_ablauf, name='check_lizenzen_ablauf'),
]