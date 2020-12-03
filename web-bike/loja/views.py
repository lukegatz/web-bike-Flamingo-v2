from django.shortcuts import *


# Essa view abre a homepage do site
def home(request):
    return render(request, 'index.html')

# Essa view é utilizada apenas para testes
# def hello(request):
#     return render(request, 'dicas.html')



