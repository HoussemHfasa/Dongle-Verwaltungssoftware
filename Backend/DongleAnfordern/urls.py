from django.urls import path
from .views import (
    TicketCreateView,
)
path("Dongleticket/create/", TicketCreateView.as_view(), name="Dongleticket_create"),