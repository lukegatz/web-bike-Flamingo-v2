from django.views.generic import ListView, DetailView

from .models import *

# Views dos produtos
# Pegamos as referências do modelo 'Bicicleta'
class BicicletaList(ListView):
    queryset = Bicicleta.objects.all()
    template = 'produtos/produtos.html'
    context_object_name = 'bicicletas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bicicleta'] = self.queryset
        return context


class BicicletaDetail(DetailView):
    model = Bicicleta
    context_object_name = 'bicicleta'
    template = 'produtos/detail-bicicleta.html'

