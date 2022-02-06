import requests
from time import sleep
from django.core.management.base import BaseCommand
from pokemon.models import Pokemon

class Command(BaseCommand):
  def handle(self, *args, **options ):
     api = requests.get("https://pokeapi.co/api/v2/pokemon?offset=20&limit=20").json()
     #breakpoint()
     for pokemon in api["results"]:
       print(pokemon)
       Pokemon.objects.get_or_create(name = pokemon["name"], urlpokemon = pokemon["url"])
    
