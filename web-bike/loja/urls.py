# urls da loja (web-bike, produtos) aqui
from django.urls import path

from .views import cliente

urlpatterns = [
    path('<str:nome>/', cliente),
]