# Generated by Django 2.2.1 on 2019-05-09 01:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=80)),
                ('senha', models.CharField(max_length=15)),
                ('cpf', models.CharField(max_length=14)),
                ('cargo', models.CharField(max_length=15)),
                ('endereco', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=10)),
                ('ativo', models.BooleanField(default=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='funcionarios/funcionarios_fotos')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
