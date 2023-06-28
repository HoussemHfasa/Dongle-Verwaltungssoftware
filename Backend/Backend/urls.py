from Dongle_hinzufügen.views import DongleCreateView
from Lizenzhinzufügen.views import LizenzCreateView
from LizenzAnfordern.views import TicketCreateView
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from User_loggin.api import UserLoginAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("", include("homepage.urls")),
    path("", include("benachrichtigung.urls")),
    path("", include("Lizenzseite.urls")),
    path('', include('User_loggin.urls')),  
    path("api/login", UserLoginAPIView.as_view(), name="api-login"),
    path("", include("Adminseite.urls")),
    path('api/', include('Dongle_hinzufügen.urls')),
    path('api/', include('Lizenzhinzufügen.urls')),
    path('api/', include('LizenzAnfordern.urls')),
    ]
    
