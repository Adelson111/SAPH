
from django.db import models
from django.urls import reverse
# Create your models here.
from apps.item.models import Item
from apps.nivel.models import Nivel


class Solicitacao(models.Model):
    tipo = models.CharField(max_length=80)
    nivel = models.ManyToManyField(Nivel, related_name='nivel_solicitacao')
    descricao = models.CharField(max_length=300, null=False)
    solicitacaoDelegacao = models.CharField(max_length=20, null=False)
    itens = models.ManyToManyField(Item, related_name='itens_solicitacao')

    def __str__(self):
        return self.tipo

    def get_absolute_url(self):
        return reverse('cadasrtrar_solicitacao')

    class Meta:
        verbose_name_plural = 'Solicitações'






