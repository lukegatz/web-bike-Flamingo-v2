# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import *
import json


"""
A view home é a responsável por renderizar a homepage do site.
"""
def home(request):
    return render(request, 'index.html')


# Essa view é utilizada apenas para testes (hello world)
# def hello(request):
#     return render(request, 'dicas.html')

"""
Essa view é responsável por se comunicar com o carrinho de compras. Por padrão, 
a view retorna Json para o navegador.
"""
def updateItem(request):
    # print(request)
    data = json.loads(request.body)
    # id do produto
    productId = data['productId']
    # a ação que será executada
    action = data['action']

    print('Id do produto:', productId)
    print('Ação:', action)

    return JsonResponse("Produto incluído no carrinho!", safe=False,
                        json_dumps_params={'ensure_ascii': False})


