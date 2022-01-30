from unicodedata import name
from django.shortcuts import render
from .models import Pokemon



def home(request):

  pokemons = Pokemon.objects.all()

  ctx = { "pokemons":pokemons}

  return render(request, "home.html", ctx)

def detalhe(request, pk):
  pokemon = Pokemon.objects.get(id = pk)

  ctx = {"pokemon":pokemon}

  return render(request, "detalhe.html", ctx)
  





  