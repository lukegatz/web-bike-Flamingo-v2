# urls da loja (web-bike, produtos) aqui
from django.urls import path

from . import views

urlpatterns = [
    path('<str:usuario>/', views.cliente),    # deve tratar cliente logado ou não
    path('produtos/', views.lista_produtos),
]