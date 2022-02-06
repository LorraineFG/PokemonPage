from unicodedata import name
from webbrowser import get
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Pokemon(models.Model):
    
    name = models.CharField("nome", max_length=50)
    tipo = models.CharField("tipo", max_length=50, null=True, blank=True) 
    habilidade = models.CharField("habilidade", max_length=200, null="lutar", blank=True) 
    urlimagem = models.URLField(null= True, blank= True)
    urlpokemon = models.URLField(_("Detalhe Pokemon"), max_length=200, null= True, blank= True)

    class Meta:
        verbose_name = ("Pokemon")
        verbose_name_plural = ("Pokemons")

    def __str__(self):
        return self.name
      