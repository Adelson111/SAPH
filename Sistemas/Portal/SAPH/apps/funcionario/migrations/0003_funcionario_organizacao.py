# Generated by Django 2.2.1 on 2019-05-16 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizacao', '0001_initial'),
        ('funcionario', '0002_auto_20190515_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='organizacao',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='organizacao', to='organizacao.Organizacao'),
            preserve_default=False,
        ),
    ]
