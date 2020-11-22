# urls da loja (web-bike, produtos) aqui
from django.urls import path

from . import views

urlpatterns = [
    # deve tratar cliente logado ou não
    path('<str:usuario>/', views.cliente),
]