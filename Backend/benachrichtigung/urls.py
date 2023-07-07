
from django.urls import path
from .utils import check_lizenzen_ablauf  
from . import views

urlpatterns = [
    path('benachrichtigung/', check_lizenzen_ablauf, name='check_lizenzen_ablauf'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/<str:firmcode>/', views.tickets_by_firmcode, name='tickets_by_firmcode'),
]