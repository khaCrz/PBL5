from django.urls import path, include
from .views import Home, Main
urlpatterns = [
    path('', Home, name='home'),
    path('main', Main, name='main'),
]