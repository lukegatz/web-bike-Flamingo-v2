from django.urls import path
from .views import BicicletaList, BicicletaDetail


'''
Esses são os paths do app 'produtos' de web-bike. Ambos referenciam classes
definidas nas views, e seguem o padrão estabelecido pelo arquivo central de
urls (em 'flamingo.urls')
O path 'bicicletas' responde à requisição 'produtos/'.
O path 'detalhe-bicicletas' recebe um slug (como definido na view correspondente)
e o acessa 'produtos/<slug>'.
'''
urlpatterns = [
    path('', BicicletaList.as_view(), name='bicicletas'),
    path('<slug>/', BicicletaDetail.as_view(), name='detalhe-bicicletas'),
]
