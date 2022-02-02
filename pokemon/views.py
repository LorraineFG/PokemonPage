from unicodedata import name
from django.shortcuts import render
from .models import Pokemon

import requests


def home(request):

  pokemons = Pokemon.objects.all()
  api = requests.get("https://pokeapi.co/api/v2/pokemon?offset=20&limit=20")

  ctx = { "pokemons":pokemons, "api":api.json}

  return render(request, "home.html", ctx)

def detalhe(request, pk):
  pokemon = Pokemon.objects.get(id = pk)

  ctx = {"pokemon":pokemon}

  return render(request, "detalhe.html", ctx)
  





  