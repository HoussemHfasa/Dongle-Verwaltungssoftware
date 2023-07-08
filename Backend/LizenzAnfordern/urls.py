from django.urls import path
from .views import (
    TicketCreateViewL ,
    TicketAnnehmenView,
    TicketAblehnenView,
    TicketDetailsView,  # freeyassin
)

urlpatterns = [
    path("ticket/create/Lizenz/", TicketCreateViewL.as_view(), name="Lizenz_ticket_create"),
    path("ticket/annehmen/", TicketAnnehmenView.as_view(), name="ticket_annehmen"),
    path("ticket/ablehnen/", TicketAblehnenView.as_view(), name="ticket_ablehnen"),
    path("ticket/details/", TicketDetailsView.as_view(), name="ticket_details"),  # yassin
    path("ticket/details/<int:id_ticket>/", TicketDetailsView.as_view(), name="ticket_details"),#yassin
]