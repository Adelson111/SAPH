# Generated by Django 2.2.1 on 2019-05-30 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionario', '0001_initial'),
        ('organizacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='funcionario_do_nivel', to='funcionario.Funcionario')),
                ('nivelInferior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nivelinferior', to='nivel.Nivel')),
                ('nivelSuperior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nivelsuperior', to='nivel.Nivel')),
                ('organizacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='organizacao_do_nivel', to='organizacao.Organizacao')),
            ],
            options={
                'verbose_name_plural': 'Niveis',
            },
        ),
    ]