from django.shortcuts import render

from django.shortcuts import render


# Views do módulo blog (curiosidades, dicas, notícias)
'''
A view curiosidades renderiza o template curiosidades.html
'''
def curiosidades(request):
    return render(request, 'curiosidades.html')


'''
A view dicas renderiza o template dicas.html
'''
def dicas(request):
    return render(request, 'dicas.html')


'''
A view noticias renderiza o template noticias.html
'''
def noticias(request):
    return render(request, 'noticias.html')

