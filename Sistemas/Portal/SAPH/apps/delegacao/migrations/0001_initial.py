# Generated by Django 2.2.1 on 2019-05-19 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('solicitacao', '0002_solicitacao_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delegacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
                ('descricao', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=15)),
                ('itens', models.ManyToManyField(to='solicitacao.Item')),
            ],
        ),
    ]
