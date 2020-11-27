from django.urls import path
from .views import BicicletaList, BicicletaDetail

urlpatterns = [
    path('', BicicletaList.as_view(), name='bicicletas'),
    path('<slug>/', BicicletaDetail.as_view(), name='detalhe-bicicletas'),
]
