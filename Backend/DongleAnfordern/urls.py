from django.urls import path
from .views import (
    TicketCreateView,
)

urlpatterns = [
path("Dongleticket/create/", TicketCreateView.as_view(), name="Dongleticket_create"),
]