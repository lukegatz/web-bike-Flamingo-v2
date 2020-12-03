from django.db import models
from loja.models import Pessoa


# Modelos do módulo Cliente
class Cliente(Pessoa):
    usuario = models.CharField(verbose_name="Usuario", max_length=15, unique=True, null=True)
    senha = models.CharField(verbose_name="Senha", max_length=15, null=True)
    # sexo
    # altura
    # peso
    # enderecoEntrega

    def __str__(self):
        return self.nome


