from django.db import models
from django.contrib.auth.models import User
from perfil.models import Pessoa


# Modelos do módulo Cliente
"""
A classe Cliente herda Pessoa, e representa qualquer cliente do site.
"""
class Cliente(Pessoa):
    user = models.OneToOneField(User, null=True, unique=True, verbose_name="Usuário",
                                on_delete=models.CASCADE)
    # models.CharField(verbose_name="Usuário", max_length=15, unique=True, null=True)
    # sexo
    # altura
    # peso
    # enderecoEntrega

    def __str__(self):
        return self.nome



