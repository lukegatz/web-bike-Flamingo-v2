# registrar as urls do blog (social media) aqui
from django.urls import path

from .views import *

urlpatterns = [
    path('posts/', posts),
    path('post/<int:id>', post),
    path('dicas/', dicas, name='dicas'),
    path('curiosidades/', curiosidades, name='curiosidades'),
    path('noticias/', noticias, name='noticias'),
]