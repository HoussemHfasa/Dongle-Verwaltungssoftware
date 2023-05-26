from .views import DongleView  
from django.urls import path  
  
urlpattern = [  
    path('homepage/', DongleView.as_view())  
]  