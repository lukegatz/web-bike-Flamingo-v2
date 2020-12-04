from django.db import models

# Modelos relativos aos PRODUTOS
"""
A classe Parcelamento representa o parcelamento a ser concedido sobre
o produto.
"""
class Parcelamento(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=12, null=True)
    quantidadeParcelas = models.PositiveIntegerField
    valorParcela = models.DecimalField(decimal_places=2, max_digits=8, null=True)


"""
A classe Produto armazena as informaçõe comuns a todos os produtos disponíveis
para venda no site.
"""
class Produto(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=12, null=True)
    descricao = models.CharField(verbose_name="Descrição do produto",
                                 max_length=144, null=True)
    imagem = models.ImageField(upload_to='produtos/static/imgs/', default=None, null=True)
    preco = models.DecimalField(decimal_places=2, max_digits=8, null=True )
    quantidade = models.PositiveIntegerField
    desconto = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    marca = models.CharField(verbose_name="Marca", max_length=40, null=True)
    slug = models.SlugField(null=True)
    #  parcelamento = models.ForeignKey(Parcelamento, on_delete=models.CASCADE)
    eParcelavel = models.BooleanField(default=False)  # apenas para parcelamento especial
    recebeDesconto = models.BooleanField(default=False)  # apenas para desconto especial

    class Meta:
        verbose_name = ('Produto')
        verbose_name_plural = ('Produtos')
        ordering = ['codigo']


# Classes que herdam Produto
# Incluir categoria para bicicletas!!
"""
A classe Bicicleta herda Produto, e representa qualquer tipo de bicicleta disponível
para venda no site.
"""
class Bicicleta(Produto):
    modelo = models.CharField(verbose_name="Modelo", max_length=60, null=True)
    # tipo
    # aro
    # tamanho_quadro
    # cor
    # categoria

    class Meta:
        verbose_name = ('Bicicleta')
        verbose_name_plural = ('Bicicletas')

    def __str__(self):
        return self.modelo


# Classe Roupa é abstrata
"""
A classe Roupa é abstrata, e será implementada por várias classes concretas que herdam
Roupa (Camisa, Bretelle, Bermuda etc.)
"""
class Roupa(Produto):
    GENEROS_ESCOLHA = (
        (u'masc', u'masculino'),
        (u'fem', u'feminino'),
    )
    genero = models.CharField(verbose_name="Gênero", max_length=4,
                              choices=GENEROS_ESCOLHA, null=True)
    # tamanho

    class Meta:
        abstract = True
        ordering = ['nome']


# class Camisa(Roupa):
    # apenas os atributos herdados das superclasses


# class Acessorio(Produto):
#     marca = models.CharField(verbose_name="Marca", max_length=40)


# class CaixaDeFerramentas(Acessorio):
    # atributos?


# class Ciclocomputador(Acessorio):
    # atributos?

"""
A classe Componente é abstrata, e será implementada por classes concretas que
herdem Componente (Cassete, Pedivela, Guidão etc.)
"""
class Componente(Produto):
    class Meta:
        abstract = True
        ordering = ['nome']


# class Cassete(Componente):
    # atributos?