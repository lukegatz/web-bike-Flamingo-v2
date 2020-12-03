# urls dos mapas
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mapas, name='mapas'),
]