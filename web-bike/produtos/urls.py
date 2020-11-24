from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista-produtos'),
    path(r'detalhe_produtos/', views.detalhe_produtos, name='detalhe-produtos')
]
