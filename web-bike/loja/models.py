from django.db import models

# Modelos gerais da loja
from django.forms import forms


class Endereco(models.Model):
    logradouro = models.CharField(verbose_name="Endereço", max_length=60)
    numero = models.CharField(verbose_name="Número", max_length=10)
    complemento = models.CharField(verbose_name="Complemento", max_length=50)
    cidade = models.CharField(verbose_name="Cidade", max_length=30)
    estado = models.CharField(verbose_name="Estado", max_length=2)
    # CEP = # essa implementação exige form -- áèóúüë
    pais = models.CharField(verbose_name="País", max_length=30)


class Telefone(models.Model):
    TIPOS_TELEFONE_ESCOLHA = (
        (u'cel', u'celular'),
        (u'res', u'residencial'),
        (u'com', u'comercial')
    )
    tipo = models.CharField(verbose_name="Tipo do telefone", max_length=3, choices=TIPOS_TELEFONE_ESCOLHA)
    numero = models.CharField(verbose_name="Número", max_length=12) # mascara?


class Pessoa(models.Model):
    nome = models.CharField("Nome: ", max_length=40)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)
    # email = # essa implementação exige form -- 'usuario'@aol.com'
    # cpf = # essa implementação exige form -- '999.999.999-99'
    dataNascimento = models.DateField

    class Meta:
        abstract = True
        ordering = ['nome']


class Cliente(Pessoa):
    usuario = models.CharField(verbose_name="Usuario", max_length=15, unique=True)
    senha = models.CharField("Senha: ", max_length=15)
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
    codigo = models.CharField(verbose_name="Código", max_length=12)
    quantidadeParcelas = models.PositiveIntegerField
    valorParcela = models.DecimalField(decimal_places=2, max_digits=8)


class Produto(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=12)
    descricao = models.CharField(verbose_name="Descrição do produto", max_length=144)
    imagem = models.ImageField(upload_to='imgs', default=None)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    quantidade = models.PositiveIntegerField
    desconto = models.DecimalField(decimal_places=2, max_digits=4)
    parcelamento = models.ForeignKey(Parcelamento, on_delete=models.CASCADE)
    eParcelavel = models.BooleanField
    recebeDesconto = models.BooleanField


class ItemInventario(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=12)
    quantidadeEmEstoque = models.PositiveIntegerField(verbose_name="Quantidade")


class Pagamento(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=12)
    valorTotal = models.DecimalField(decimal_places=2, max_digits=8)


class Pedido(models.Model):
    data_do_pedido = models.DateTimeField(auto_now_add=True)

# Pedido
# ParcelamentoEspecial
# DescontoEspecial
# AnuncioEspecial
