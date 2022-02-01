from django.contrib import admin
from .models import Pokemon 

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    model = Pokemon
    list_display = ("id", "name", "tipo", "habilidade")
    