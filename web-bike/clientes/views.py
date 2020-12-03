# arquivo de views do módulo Clientes
from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Cliente


# Teste para leitura de dados do BD
def ler_cliente(usuario):
    clientes = Cliente.objects.filter(usuario=usuario)

    for cliente in clientes:
        return cliente
    else:
        return None


# View para retornar dados do cliente
def cliente(request, usuario):
    # o user já é o próprio name (o Cliente retorna name por padrão)
    user = ler_cliente(usuario)

    if user is not None:
        # outro atributo tem que ser pego com __getattribute__('chave')
        passw = ler_cliente(usuario).__getattribute__('senha')
        context = {'v_user': user, 'v_passw': passw}
        return render(request, 'clientes/cliente.html', context)
    else:
        raise Http404("Pessoa naum encontrada... :(")


# deve retornar o formulário para criação de cadastro de cliente
def criarCliente(self, request):

    valor_contexto = {}

    return render(request, 'criar_cliente.html', context=valor_contexto)

