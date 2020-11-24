from django.shortcuts import render
from .models import *

# Views dos produtos
# Pegamos as referências do modelo 'Bicicleta'
bike_refs = Bicicleta.objects.all()

def lista_produtos(request):
    # Empacotamos as referências da Bicicleta, para enviar com o render
    context = {'produtos': bike_refs}
    return render(request, 'produtos/produtos.html', context)


def detalhe_produtos(request):
    context = {'produtos': bike_refs}
    return render(request, 'produtos/detalhe-produtos.html', context)


# def detalhe_produtos(request, modelo):
#     context = {'produtos': bike_refs}
#     for bk in context:
#         if bk.modelo == modelo.modelo:
#             bike = bk
#
#     bike = {'bicicleta': bike}
#     return render(request, 'produtos/detalhe-produtos.html', bike)