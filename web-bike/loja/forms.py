# formulários da loja são criados aqui
from django import forms

from bike_site.models import Cliente


class UserForm(forms.ModelForms):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'usuario',
            'senha'
        ]
        widget = {
            'senha': forms.PasswordInput(),
        }

