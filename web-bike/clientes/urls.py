# urls do módulo de clientes
from django.urls import path
from . import views


"""
O path do módulo 'clientes', que responde ao padrão 'clientes/<usuario>/'.
"""
urlpatterns = [
    # deve tratar cliente logado ou não
    path('<str:usuario>/', views.cliente),
]