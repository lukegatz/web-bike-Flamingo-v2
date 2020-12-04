# Generated by Django 3.1.3 on 2020-12-04 01:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='senha',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='usuario',
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(max_length=100, null=True, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]