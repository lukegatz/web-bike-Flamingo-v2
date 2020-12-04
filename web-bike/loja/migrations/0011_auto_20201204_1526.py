# Generated by Django 3.1.3 on 2020-12-04 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_auto_20201204_0104'),
        ('perfil', '0001_initial'),
        ('loja', '0010_auto_20201204_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='endereco',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perfil.endereco'),
        ),
        migrations.AddField(
            model_name='vendedor',
            name='telefone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='perfil.telefone'),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='produto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produtos.bicicleta'),
        ),
    ]