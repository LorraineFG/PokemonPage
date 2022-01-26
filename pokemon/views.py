from unicodedata import name
from django.shortcuts import render
from .models import Pokemon



def home(request):

  pokemons = Pokemon.objects.all()

  ctx = { "pokemons":pokemons}

  return render(request, "home.html", ctx)





  