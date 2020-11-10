from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import Cliente

# Essa view abre a homepage do site
def home(request):
    return render(request, 'index.html')


def hello(request):
    return render(request, 'index_teste.html')


# Teste para leitura de dados do BD
def ler_cliente(nome):
    clientes = Cliente.objects.all()

    for pessoa in clientes.values():
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return HttpResponse("Pessoa naum encontrada... :(")


# View para retornar dados do cliente
# (retirada da versao final!!!!)
def cliente(request, nome):
    try:
        user = ler_cliente(nome)['usuario']
        passw = ler_cliente(nome)['senha']
    except KeyError:
        return HttpResponse("Pessoa naum encontrada... :(")
    return render(request, 'cliente.html', {'v_user': user, 'v_passw': passw})
