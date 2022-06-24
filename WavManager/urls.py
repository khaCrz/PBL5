from django.urls import path, include
from .views import Home, Main, GetText
urlpatterns = [
    path('', Home, name='home'),
    path('main', Main, name='main'),
    path('GetText', GetText, name='gettext'),
]