from rest_framework import generics
from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonListCreate(generics.ListCreateAPIView):
    queryset = Pokemon.objetos.all()
    serializer_class = PokemonSerializer

class PokemonRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokemon.objetos.all()
    serializer_class = PokemonSerializer