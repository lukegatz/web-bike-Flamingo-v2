from django.db import models

# Modelos relativos aos PRODUTOS
class Parcelamento(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=12, null=True)
    quantidadeParcelas = models.PositiveIntegerField
    valorParcela = models.DecimalField(decimal_places=2, max_digits=8, null=True)


class Produto(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=12, null=True)
    descricao = models.CharField(verbose_name="Descrição do produto",
                                 max_length=144, null=True)
    imagem = models.ImageField(upload_to='produtos/static/imgs/', default=None, null=True)
    preco = models.DecimalField(decimal_places=2, max_digits=8, null=True )
    quantidade = models.PositiveIntegerField
    desconto = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    marca = models.CharField(verbose_name="Marca", max_length=40, null=True)
    #  parcelamento = models.ForeignKey(Parcelamento, on_delete=models.CASCADE)
    eParcelavel = models.BooleanField
    recebeDesconto = models.BooleanField


class ItemInventario(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=12, null=True)
    quantidadeEmEstoque = models.PositiveIntegerField(verbose_name="Quantidade",
                                                      null=True)


# Classes que herdam Produto
class Bicicleta(Produto):
    modelo = models.CharField(verbose_name="Modelo", max_length=60, null=True)
    # tipo
    # aro
    # tamanho_quadro
    # cor

    def __str__(self):
        return self.modelo


# Classe Roupa é abstrata
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


class Componente(Produto):
    class Meta:
        abstract = True
        ordering = ['nome']


# class Cassete(Componente):
    # atributos?