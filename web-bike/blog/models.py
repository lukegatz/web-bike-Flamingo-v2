from django.db import models

from loja.models import Pessoa, Vendedor

# Aqui estão armazenados os modelos do blog (social media)

class SocialMedia(Pessoa):
    # apenas os campos das superclasses
    def __init__(self):
        self.vendedor = Vendedor()

    def __str__(self):
        return self.nome

# class Post
# especializações? (Dica, Notícia, etc.)

# class Mapa
# classe de integração apenas?