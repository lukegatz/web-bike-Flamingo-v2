from django.db import models

from loja.models import Pessoa, Vendedor

# Aqui estão armazenados os modelos do blog (social media)
"""
O usuário SocialMedia herda a classe Pessoa e faz composição com Vendedor.
SocialMedia é o usuário com responsabilidades sobre os conteúdos textuais do
site (permissões de acesso são definidas no módulo administrativo).
"""
class SocialMedia(Pessoa):
    # apenas os campos das superclasses
    def __init__(self):
        self.vendedor = Vendedor()

    def __str__(self):
        return self.nome

