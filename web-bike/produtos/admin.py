from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Bicicleta)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('modelo',), }


