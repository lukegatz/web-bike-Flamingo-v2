from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
def posts(args):
    pass


def post(args):
    pass


def dicas(request):
    return render(request, 'dicas.html')


def curiosidades(request):
    return render(request, 'curiosidades.html')


def noticias(request):
    return render(request, 'noticias.html')

