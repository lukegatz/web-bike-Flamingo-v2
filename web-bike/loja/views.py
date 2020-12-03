from django.shortcuts import *


'''
A view home é a responsável por renderizar a homepage do site.
'''
def home(request):
    return render(request, 'index.html')


# Essa view é utilizada apenas para testes (hello world)
# def hello(request):
#     return render(request, 'dicas.html')



