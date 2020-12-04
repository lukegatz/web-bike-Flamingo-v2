from django.db import models

# Modelos básicos para a criação de perfis
"""
A classe Endereco representa qualquer endereço necessário para as classes de pessoal 
(Cliente, Vendedor, Gerente e SocialMedia).
"""
class Endereco(models.Model):
    logradouro = models.CharField(verbose_name="Endereço", max_length=60, null=True)
    numero = models.CharField(verbose_name="Número", max_length=10, null=True)
    complemento = models.CharField(verbose_name="Complemento", max_length=50, null=True)
    cidade = models.CharField(verbose_name="Cidade", max_length=30, null=True)
    estado = models.CharField(verbose_name="Estado", max_length=2, null=True)
    # CEP = # essa implementação exige form -- áèóúüë
    pais = models.CharField(verbose_name="País", max_length=30, null=True)


"""
A classe Telefone representa qualquer telefone necessário para as classes de pessoal 
(Cliente, Vendedor, Gerente e SocialMedia).
"""
class Telefone(models.Model):
    TIPOS_TELEFONE_ESCOLHA = (
        (u'cel', u'celular'),
        (u'res', u'residencial'),
        (u'com', u'comercial')
    )
    tipo = models.CharField(verbose_name="Tipo do telefone", max_length=3,
                            choices=TIPOS_TELEFONE_ESCOLHA, null=True)
    numero = models.CharField(verbose_name="Número", max_length=12, null=True) # mascara?


"""
A classe Pessoa é abstrata, e traz as informações comuns para a entidade Pessoa, tais
como nome, número do documento etc.
"""
class Pessoa(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=40, null=True)
    email = models.CharField(verbose_name="E-mail", max_length=100, null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE, null=True)
    # cpf = # essa implementação exige mask -- '999.999.999-99'
    dataNascimento = models.DateField

    class Meta:
        abstract = True
        ordering = ['nome']


