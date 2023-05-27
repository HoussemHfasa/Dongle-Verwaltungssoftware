from django.urls import path
from .views import LizenzView

urlpatterns = [
    path('Lizenzseite/', LizenzView.as_view()),
]