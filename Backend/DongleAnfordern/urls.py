from django.urls import path
from .views import (
    TicketCreateViewD,
)

urlpatterns = [
path("Dongleticket/create/", TicketCreateViewD.as_view(), name="Dongleticket_create"),
]