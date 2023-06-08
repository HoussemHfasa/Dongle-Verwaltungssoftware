from django.urls import path
from .views import CustomuserView

urlpatterns = [
    path('Adminseite/', CustomuserView.as_view()),
]