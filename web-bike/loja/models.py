from django.db import models
from perfil.models import Pessoa
from clientes.models import Cliente
from produtos.models import Produto, Bicicleta


# Modelos gerais da loja
"""
A classe Vendedor herda Pessoa, e representa um vendedor do site.
"""
class Vendedor(Pessoa):
    # codigo
    # permissoes
    # comissao

    class Meta:
        verbose_name = ('Vendedor')
        verbose_name_plural = ('Vendedores')

    def __str__(self):
        return self.nome


"""
A classe Gerente especializa Vendedor, e representa um Gerente do site.
"""
class Gerente(Vendedor):
    # apenas os campos das superclasses

    class Meta:
        verbose_name = ('Gerente')
        verbose_name_plural = ('Gerentes')

    def __str__(self):
        return self.nome


"""
A classe Pagamento é uma abstração do método de pagamento a ser aplicado no Pedido.
"""
class Pagamento(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=12, null=True)
    valorTotal = models.DecimalField(decimal_places=2, max_digits=8, null=True)


"""
A classe Pedido é a representação de um Pedido feito no site.
"""
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    data_do_pedido = models.DateTimeField(auto_now_add=True, null=True)
    completo = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = ('Pedido')
        verbose_name_plural = ('Pedidos')
        ordering = ['data_do_pedido']

    def __str__(self):
        return str(self.id)


"""
A classe ItemPedido encapsula a lógica dos itens que são adicionados ao pedido.
"""
class ItemPedido(models.Model):
    produto = models.ForeignKey(Bicicleta, on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    data_adicionado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ('Item do pedido')
        verbose_name_plural = ('Itens do pedido')
        ordering = ['data_adicionado']


"""
ItemInventario representa a conexão do sistema de vendas com o sistema de estoque.
"""
class ItemInventario(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=12, null=True)
    quantidadeEmEstoque = models.PositiveIntegerField(verbose_name="Quantidade",
                                                      null=True)

    class Meta:
        verbose_name = ('Item do inventário')
        verbose_name_plural = ('Itens do inventário')




# ParcelamentoEspecial
# DescontoEspecial
# AnuncioEspecial
