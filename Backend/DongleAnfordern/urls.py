from django.urls import path
from .views import (
    TicketCreateViewD,
    TicketCreateViewL
)

urlpatterns = [
path("Dongleticket/create/", TicketCreateViewD.as_view(), name="Dongleticket_create"),
path("Lizenzticket/create/", TicketCreateViewL.as_view(), name="Lizenzticket_create"),
]