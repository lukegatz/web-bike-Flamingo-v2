from django.views.generic import ListView, DetailView

from .models import *

# Views dos produtos
'''
A class view BicicletaList é uma implementação de uma ListView, e retorna
todos os produtos do banco de dados (a lógica do que deve ser retornado
é armazenada no queryset).
Note que, por padrão, essa view será renderizada como bicicleta_list (o nome da classe).
'''
class BicicletaList(ListView):
    queryset = Bicicleta.objects.all()
    # template = 'produtos/produtos.html'
    context_object_name = 'bicicletas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bicicleta'] = self.queryset
        return context

'''
A classe BicicletaDetail, que herda DetailView traz as informações em detalhe
de algum item do model (aqui no caso, o model Bicicleta). A renderização se dá
por meio do acesso ao id ou ao slug (como é o caso aqui).
'''
class BicicletaDetail(DetailView):
    model = Bicicleta
    template_name = 'produtos/detalhe-bicicletas.html'
    context_object_name = 'bicicleta'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detalhe = Bicicleta.objects.filter(slug=self.kwargs.get('slug'))

        return context

