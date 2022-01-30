from django.urls import path

from .views import home, detalhe

urlpatterns = [
    path("", home, name="home"),
    path("<int:pk>/", detalhe, name="detalhe"),

  ]
