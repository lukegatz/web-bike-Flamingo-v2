# urls dos mapas
from django.urls import path
from . import views

'''
O path definido em mapas.urls responde ao padrão 'mapas/'
'''
urlpatterns = [
    path('', views.mapas, name='mapas'),
]