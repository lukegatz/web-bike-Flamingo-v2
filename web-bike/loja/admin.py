from django.contrib import admin

from .models import Cliente, Gerente, Produto, Vendedor

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Gerente)
admin.site.register(Produto)
admin.site.register(Vendedor)

