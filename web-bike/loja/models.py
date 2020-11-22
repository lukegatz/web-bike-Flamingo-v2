from django.db import models
from django.forms import forms


# Modelos gerais da loja
class Endereco(models.Model):
    logradouro = models.CharField(verbose_name="Endereço", max_length=60, null=True)
    numero = models.CharField(verbose_name="Número", max_length=10, null=True)
    complemento = models.CharField(verbose_name="Complemento", max_length=50, null=True)
    cidade = models.CharField(verbose_name="Cidade", max_length=30, null=True)
    estado = models.CharField(verbose_name="Estado", max_length=2, null=True)
    # CEP = # essa implementação exige form -- áèóúüë
    pais = models.CharField(verbose_name="País", max_length=30, null=True)


class Telefone(models.Model):
    TIPOS_TELEFONE_ESCOLHA = (
        (u'cel', u'celular'),
        (u'res', u'residencial'),
        (u'com', u'comercial')
    )
    tipo = models.CharField(verbose_name="Tipo do telefone", max_length=3,
                            choices=TIPOS_TELEFONE_ESCOLHA, null=True)
    numero = models.CharField(verbose_name="Número", max_length=12, null=True) # mascara?


class Pessoa(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=40, null=True)
    # endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    # telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)
    # email = # essa implementação exige form -- 'usuario'@aol.com'
    # cpf = # essa implementação exige form -- '999.999.999-99'
    dataNascimento = models.DateField

    class Meta:
        abstract = True
        ordering = ['nome']


class Cliente(Pessoa):
    usuario = models.CharField(verbose_name="Usuario", max_length=15, unique=True, null=True)
    senha = models.CharField(verbose_name="Senha", max_length=15, null=True)
    # sexo
    # altura
    # peso
    # enderecoEntrega

    def __str__(self):
        return self.nome


class Vendedor(Pessoa):
    # codigo
    # permissoes
    # comissao

    def __str__(self):
        return self.nome


class Gerente(Vendedor):
    # apenas os campos das superclasses

    def __str__(self):
        return self.nome


class Parcelamento(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=12, null=True)
    quantidadeParcelas = models.PositiveIntegerField
    valorParcela = models.DecimalField(decimal_places=2, max_digits=8, null=True)


class Produto(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=12, null=True)
    descricao = models.CharField(verbose_name="Descrição do produto",
                                 max_length=144, null=True)
    imagem = models.ImageField(upload_to='loja/static/imgs', default=None, null=True)
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


class Pagamento(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=12, null=True)
    valorTotal = models.DecimalField(decimal_places=2, max_digits=8, null=True)


# Pedido
class Pedido(models.Model):
    data_do_pedido = models.DateTimeField(auto_now_add=True, null=True)


# ParcelamentoEspecial


# DescontoEspecial


# AnuncioEspecial


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