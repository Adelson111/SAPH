# Generated by Django 2.2.1 on 2019-05-17 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
                ('descricao', models.CharField(max_length=300)),
                ('itens', models.ManyToManyField(null=True, related_name='itens_solicitacao', to='solicitacao.Item')),
            ],
            options={
                'verbose_name_plural': 'Solicitações',
            },
        ),
    ]