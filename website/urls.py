from . import views
from django.urls import path
from website.views import ListaPokemons

app_name = 'website'

urlpatterns = [    
    path('pokedex/', ListaPokemons.as_view(), name='pokedex')
]