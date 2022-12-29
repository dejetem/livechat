

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lobby/', views.lobby, name='lobby'),
    path('room/', views.room, name='room'),
    path('get_token/', views.getToken, name='get_token'),
    path('create_member/', views.createUser, name='create_member'),
    path('get_member/', views.getUser, name='get_member'),
    path('delete_member/', views.deleteUser, name='delete_member'),
]