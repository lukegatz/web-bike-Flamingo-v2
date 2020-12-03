from django.db import models
from django.forms import forms


# Modelos gerais da loja
'''
A classe Endereco representa qualquer endereço necessário para as classes de pessoal 
(Cliente, Vendedor, Gerente e SocialMedia).
'''
class Endereco(models.Model):
    logradouro = models.CharField(verbose_name="Endereço", max_length=60, null=True)
    numero = models.CharField(verbose_name="Número", max_length=10, null=True)
    complemento = models.CharField(verbose_name="Complemento", max_length=50, null=True)
    cidade = models.CharField(verbose_name="Cidade", max_length=30, null=True)
    estado = models.CharField(verbose_name="Estado", max_length=2, null=True)
    # CEP = # essa implementação exige form -- áèóúüë
    pais = models.CharField(verbose_name="País", max_length=30, null=True)


'''
A classe Telefone representa qualquer telefone necessário para as classes de pessoal 
(Cliente, Vendedor, Gerente e SocialMedia).
'''
class Telefone(models.Model):
    TIPOS_TELEFONE_ESCOLHA = (
        (u'cel', u'celular'),
        (u'res', u'residencial'),
        (u'com', u'comercial')
    )
    tipo = models.CharField(verbose_name="Tipo do telefone", max_length=3,
                            choices=TIPOS_TELEFONE_ESCOLHA, null=True)
    numero = models.CharField(verbose_name="Número", max_length=12, null=True) # mascara?


'''
A classe Pessoa é abstrata, e traz as informações comuns para a entidade Pessoa, tais
como nome, número do documento etc.
'''
class Pessoa(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=40, null=True)
    # endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    # telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)
    # email = # essa implementação exige mask -- 'usuario'@aol.com'
    # cpf = # essa implementação exige mask -- '999.999.999-99'
    dataNascimento = models.DateField

    class Meta:
        abstract = True
        ordering = ['nome']


'''
A classe Vendedor herda Pessoa, e representa um vendedor do site.
'''
class Vendedor(Pessoa):
    # codigo
    # permissoes
    # comissao

    class Meta:
        verbose_name = ('Vendedor')
        verbose_name_plural = ('Vendedores')

    def __str__(self):
        return self.nome


'''
A classe Gerente especializa Vendedor, e representa um Gerente do site.
'''
class Gerente(Vendedor):
    # apenas os campos das superclasses

    class Meta:
        verbose_name = ('Gerente')
        verbose_name_plural = ('Gerentes')

    def __str__(self):
        return self.nome


'''
A classe Pagamento é uma abstração do método de pagamento a ser aplicado no Pedido.
'''
class Pagamento(models.Model):
    codigo = models.CharField(verbose_name="Código", max_length=12, null=True)
    valorTotal = models.DecimalField(decimal_places=2, max_digits=8, null=True)


'''
A classe Pedido é a representação de um Pedido feito no site.
'''
class Pedido(models.Model):
    data_do_pedido = models.DateTimeField(auto_now_add=True, null=True)


# ParcelamentoEspecial


# DescontoEspecial


# AnuncioEspecial
