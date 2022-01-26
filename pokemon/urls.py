from django.urls import path

from pokemon.models import Pokemon
from .views import home

urlpatterns = [
    path("", home, name="home"),
  ]
