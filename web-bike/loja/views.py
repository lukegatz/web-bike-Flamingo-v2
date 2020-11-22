from django.shortcuts import *
from django.http import HttpResponse
from .models import *

# Essa view abre a homepage do site
def home(request):
    return render(request, 'index.html')


def hello(request):
    return render(request, 'index_teste.html')


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
        return render(request, 'cliente.html', context)
    else:
        raise Http404("Pessoa naum encontrada... :(")


# deve retornar o formulário para criação de cadastro de cliente
def criarCliente(self, request):

    valor_contexto = {}

    return render(request, 'criar_cliente.html', context=valor_contexto)


def lista_produtos(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'produtos.html', context)
