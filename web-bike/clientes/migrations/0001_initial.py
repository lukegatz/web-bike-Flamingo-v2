# Generated by Django 3.1.3 on 2020-12-02 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, null=True, verbose_name='Nome')),
                ('usuario', models.CharField(max_length=15, null=True, unique=True, verbose_name='Usuario')),
                ('senha', models.CharField(max_length=15, null=True, verbose_name='Senha')),
            ],
            options={
                'ordering': ['nome'],
                'abstract': False,
            },
        ),
    ]