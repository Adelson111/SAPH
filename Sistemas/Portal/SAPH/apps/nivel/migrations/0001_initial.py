# Generated by Django 2.2.1 on 2019-05-17 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='funcionario.Funcionario')),
                ('nivelInferior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nivelinferior', to='nivel.Nivel')),
                ('nivelSuperior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nivelsuperior', to='nivel.Nivel')),
            ],
            options={
                'verbose_name_plural': 'Niveis',
            },
        ),
    ]