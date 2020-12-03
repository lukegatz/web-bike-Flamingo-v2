from django.shortcuts import render

# Views dos mapas

def mapas(request):
    return render(request, 'mapas/mapa.html')
