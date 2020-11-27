from django.urls import path
from .views import BicicletaList, BicicletaDetail

urlpatterns = [
    path('', BicicletaList.as_view(), name='lista-produtos'),
    path(r'<slug:slug>/', BicicletaDetail.as_view(), name='detail-bicicleta'),
]
