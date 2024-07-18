from django.db import models

class Pokemon(models.Model):
    numero = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    imagem_url = models.CharField(
        default="https://static.wikia.nocookie.net/bec6f033-936d-48c5-9c1e-7fb7207e28af",
        max_length=255,
        null=False,
        blank=False
    )
    altura = models.DecimalField(
        max_digits=8,
        decimal_places=1,
        null=False,
        blank=False
    )
    peso = models.DecimalField(
        max_digits=8,
        decimal_places=1,
        null=False,
        blank=False
    )
    tipo1 = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    tipo2 = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    objetos = models.Manager()