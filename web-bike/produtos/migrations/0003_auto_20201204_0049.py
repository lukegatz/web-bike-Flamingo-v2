# Generated by Django 3.1.3 on 2020-12-04 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_auto_20201127_0334'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ItemInventario',
        ),
        migrations.AddField(
            model_name='produto',
            name='eParcelavel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='produto',
            name='recebeDesconto',
            field=models.BooleanField(default=False),
        ),
    ]