# registrar as urls do blog (social media) aqui
from django.urls import path

from blog.views import posts, post, rotas, rota

urlpatterns = [
    path('blog/posts/', posts),
    path('blog/post/<int:id>', post),
    path('blog/mapas/', rotas),
    path('blog/mapa/<str:local>', rota)
]