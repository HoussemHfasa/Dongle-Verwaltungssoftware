from django.urls import path
from .views import (UserLoginAPIView, UserListView, UserDetailView,
                    AdminListView, VerwalterListView, KundeListView)

urlpatterns = [
    #path('login/', UserLoginAPIView.as_view(), name='user-login'),  # Add this line
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('admin/', AdminListView.as_view(), name='admin-list'),
    path('verwalter/', VerwalterListView.as_view(), name='verwalter-list'),
    path('kunde/', KundeListView.as_view(), name='kunde-list'),
]