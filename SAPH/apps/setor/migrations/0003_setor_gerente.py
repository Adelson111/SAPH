# Generated by Django 2.2.1 on 2019-05-10 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
        ('setor', '0002_setor_nivel'),
    ]

    operations = [
        migrations.AddField(
            model_name='setor',
            name='gerente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gerentesetor', to='funcionario.Funcionario'),
        ),
    ]
