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


class Vendedor(Pessoa):
    # codigo
    # permissoes
    # comissao

    class Meta:
        verbose_name = ('Vendedor')
        verbose_name_plural = ('Vendedores')

    def __str__(self):
        return self.nome


class Gerente(Vendedor):
    # apenas os campos das superclasses

    class Meta:
        verbose_name = ('Gerente')
        verbose_name_plural = ('Gerentes')

    def __str__(self):
        return self.nome


class Pagamento(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=12, null=True)
    valorTotal = models.DecimalField(decimal_places=2, max_digits=8, null=True)


# Pedido
class Pedido(models.Model):
    data_do_pedido = models.DateTimeField(auto_now_add=True, null=True)


# ParcelamentoEspecial


# DescontoEspecial


# AnuncioEspecial
