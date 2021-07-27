from django import template
import locale

# Register template?
register = template.Library()

'''
A template tag precificar aplica o formato de preço ao valor float 
(no caso, definimos pt_BR como padrão a ser aplicado)
'''
@register.filter(name='precificar')
def precificar(valor):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    # locale.setlocale(locale.LC_ALL, 'en_US')
    valor = locale.currency(valor, grouping=True)
    return valor



