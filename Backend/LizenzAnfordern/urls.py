from django.urls import path
from .views import TicketCreateView

urlpatterns = [
    path('ticket/create/', TicketCreateView.as_view(), name='ticket-create'),
]