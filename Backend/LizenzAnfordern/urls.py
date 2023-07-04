from django.urls import path
from .views import TicketCreateView, TicketAnnehmenView, TicketAblehnenView

urlpatterns = [
    path('ticket/create/', TicketCreateView.as_view(), name='ticket-create'),
    path('ticket/annehmen/', TicketAnnehmenView.as_view(), name='ticket-annehmen'),
    path('ticket/ablehnen/', TicketAblehnenView.as_view(), name='ticket-ablehnen'),
]