from django.shortcuts import render

# Views dos mapas
'''
A view mapas renderiza o template 'mapas/mapa.html'
'''
def mapas(request):
    return render(request, 'mapas/mapa.html')
