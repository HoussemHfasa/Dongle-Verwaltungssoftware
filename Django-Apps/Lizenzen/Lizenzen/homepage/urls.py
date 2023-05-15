from django.urls import path
from . import views


urlpatterns = [
    path('mymodel/', views.MyModelListCreateView.as_view(), name='mymodel_list_create'),
    path('mymodel/<int:pk>/', views.MyModelRetrieveUpdateDestroyView.as_view(), name='mymodel_retrieve_update_destroy'),
]