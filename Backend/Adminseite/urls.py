from django.urls import path
from .views import CustomuserView

app_name = 'Adminseite'
urlpatterns = [
    path('Adminseite/', CustomuserView.as_view(), name='Adminseite'),
    path('Adminseite/delete-row/<int:pk>/', CustomuserView.as_view(), name='delete-row'),  
    path('Adminseite/<int:pk>/', CustomuserView.as_view(), name='customuser-update-delete'),
]