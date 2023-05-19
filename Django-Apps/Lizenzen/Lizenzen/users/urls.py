
from . import views
from django.urls import path
from . import views, views_api

from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('api/user_role/', views_api.user_role, name='user_role'),
]