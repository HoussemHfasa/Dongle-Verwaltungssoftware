from django.urls import path
from .views import (
    TicketAnnehmenView,
    TicketAblehnenView,
    TicketDetailsView, 
)

urlpatterns = [
    path("ticket/annehmen/", TicketAnnehmenView.as_view(), name="ticket_annehmen"),
    path("ticket/ablehnen/", TicketAblehnenView.as_view(), name="ticket_ablehnen"),
    path("ticket/details/", TicketDetailsView.as_view(), name="ticket_details"), 
    path("ticket/details/<int:id_ticket>/", TicketDetailsView.as_view(), name="ticket_details"),
]