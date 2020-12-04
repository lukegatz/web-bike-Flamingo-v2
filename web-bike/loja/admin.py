from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Gerente)
admin.site.register(Vendedor)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(ItemInventario)