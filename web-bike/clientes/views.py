# arquivo de views do módulo Clientes
from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Cliente


'''
A função ler_cliente retorna um cliente (baseado no usuário do cliente) ou
None, caso esse cliente não exista.
'''
def ler_cliente(usuario):
    clientes = Cliente.objects.filter(usuario=usuario)

    for cliente in clientes:
        return cliente
    else:
        return None


'''
A view cliente retorna os dados do cliente, fazendo uma chamada a ler_cliente para
verificar se o usuario que foi passado como parâmetro existe.
'''
def cliente(request, usuario):
    # o user já é o próprio name (o Cliente retorna name por padrão)
    user = ler_cliente(usuario)

    if user is not None:
        # outro atributo tem que ser pego com __getattribute__('chave')
        passw = ler_cliente(usuario).__getattribute__('senha')
        context = {'v_user': user, 'v_passw': passw}
        return render(request, 'clientes/cliente.html', context)
    else:
        raise Http404("Pessoa não encontrada... :(")


# deve retornar o formulário para criação de cadastro de cliente
def criarCliente(self, request):

    valor_contexto = {}

    return render(request, 'criar_cliente.html', context=valor_contexto)

