from django.urls import path
from .views import DongleCreateView

urlpatterns = [
    path('dongle/create/', DongleCreateView.as_view(), name='dongle-create'),
]