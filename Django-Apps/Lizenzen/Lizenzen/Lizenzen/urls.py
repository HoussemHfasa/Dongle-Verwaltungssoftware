"""
Definition of urls for Lizenzen.
"""

from datetime import datetime
from django.urls import path,include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from . import views, views_api
from django.urls import path
from . import views

from users.views import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
  
    #path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),  
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    #path('admin/', admin.site.urls),
 
    path('api/auth/', include('dj_rest_auth.urls')),#Api auth
   path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # auth
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),#auth
    path('api/user_role/', views_api.user_role, name='user_role'),
]
