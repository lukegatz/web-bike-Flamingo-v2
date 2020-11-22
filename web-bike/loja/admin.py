from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Gerente)
admin.site.register(Vendedor)
admin.site.register(Bicicleta)

# classes para formatação do endereço
# class EnderecoInLine(admin.StackedInline):
#     model = Endereco


# class ClienteAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['nome']}),
#         (None, {'fields': ['usuario', 'senha']}),
#     ]
#     inline = [EnderecoInLine]
#     # fieldsets = [
#     #     (None, {'fields': ['logradouro', 'numero', 'complemento']})
#     # ]
#
#
# admin.site.register(Cliente, ClienteAdmin)