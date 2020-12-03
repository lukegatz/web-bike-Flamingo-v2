# registrar as urls do blog (social media) aqui
from django.urls import path

from .views import *

'''
Os paths armazenados no módulo 'blog', que tem a responsabilidade sobre
o material textual do site (notícias, curiosidades e dicas).
Os paths estabelecidos aqui respondem à requisição 'blog/' e chamam 
a função respectiva, definida na view. 
'''
urlpatterns = [
    path('dicas/', dicas, name='dicas'),
    path('curiosidades/', curiosidades, name='curiosidades'),
    path('noticias/', noticias, name='noticias'),
]