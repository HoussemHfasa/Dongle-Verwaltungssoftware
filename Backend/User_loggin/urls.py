
from django.urls import path
from .views import user_role  # Import view directly

urlpatterns = [
    path('user_role/', user_role, name='user_role'), 
]