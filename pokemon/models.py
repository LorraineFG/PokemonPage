from distutils.command.upload import upload
from email.mime import image
from tkinter import image_types
from unicodedata import name
from django.db import models

# Create your models here.
class Pokemon(models.Model):
    
    name = models.CharField("nome", max_length=50)
    tipo = models.CharField("tipo", max_length=50, null=True, blank=True) 
    habilidade = models.CharField("habilidade", max_length=200, null="lutar", blank=True) 
    urlimagem = models.CharField("urlimage", max_length=300, null=True)

    class Meta:
        verbose_name = ("Pokemon")
        verbose_name_plural = ("Pokemons")

    def __str__(self):
        return self.name
      