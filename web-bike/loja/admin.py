from django.contrib import admin

from .models import Cliente, Gerente, Produto, Vendedor, Endereco

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Gerente)
admin.site.register(Vendedor)

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
admin.site.register(Produto)