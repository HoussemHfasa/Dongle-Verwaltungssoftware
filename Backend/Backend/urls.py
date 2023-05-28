from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from User_loggin.api import UserLoginAPIView

urlpatterns = [
    # path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('User_loggin/', include('User_loggin.urls')),
    path("", include("homepage.urls")),
<<<<<<< HEAD
    path("", include("benachrichtigung.urls")),
    path("", include("Lizenzseite.urls")),

]
=======
    path('user_loggin/', include('User_loggin.urls')),
    path('', include('User_loggin.urls')),  
    path("api/login", UserLoginAPIView.as_view(), name="api-login"),
    ]
    
>>>>>>> Houssem
