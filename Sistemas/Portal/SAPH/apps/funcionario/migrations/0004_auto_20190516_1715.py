# Generated by Django 2.2.1 on 2019-05-16 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0003_funcionario_organizacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='organizacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organizacao', to='organizacao.Organizacao'),
        ),
    ]
