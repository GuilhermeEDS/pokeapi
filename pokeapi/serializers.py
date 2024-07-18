from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['numero', 'nome', 'imagem_url', 'altura', 'peso', 'tipo1', 'tipo2']