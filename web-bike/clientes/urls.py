# urls do módulo de clientes
from django.urls import path

from . import views

urlpatterns = [
    # deve tratar cliente logado ou não
    path('<str:usuario>/', views.cliente),
]