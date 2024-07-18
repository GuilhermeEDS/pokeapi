from django.shortcuts import render
from django.views.generic import ListView
from pokeapi.models import Pokemon
# Create your views here.
#def lista_pokemons(request):
#    pokemons = Pokemon.objetos.all()
#    
#    contexto = {'pokemons': pokemons}
#    
#    return render(request, "templates/pokemons.html", contexto)


class ListaPokemons(ListView):
    template_name = "pokemons.html"
    model = Pokemon
    context_object_name = "pokemons"