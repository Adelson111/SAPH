import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from pip._vendor import requests
from apps.funcionario.models import Funcionario
from apps.item.models import Item
from apps.nivel.models import Nivel
from apps.organizacao.models import Organizacao
from apps.setor.models import Setor
from apps.solicitacao.models import Solicitacao


class MyHome(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/home.html')

class Exportar(LoginRequiredMixin, View) :

    def get(self, request):
        organizacoes = Organizacao.objects.filter(pk=request.user.funcionario.organizacao.pk).values()
        funcionairos = Funcionario.objects.filter(organizacao=self.request.user.funcionario.organizacao)
        niveis = Nivel.objects.filter(organizacao=self.request.user.funcionario.organizacao)

        lOrganizacao1 = []
        lFuncionarios = []
        lNiveis = []
        organizacaoDic = {}

        for funcionario in funcionairos:
            dic = {
                'id': funcionario.pk,
                'nome': funcionario.nome,
                'cpf': funcionario.cpf,
                'cargo': funcionario.cargo,
                'endereco': funcionario.endereco,
                'telefone': funcionario.telefone,
                'ativo': funcionario.ativo,
                'usuario': {
                    'id': funcionario.user.pk,
                    'email': funcionario.user.username,
                    'senha': funcionario.user.password
                }
            }
            lFuncionarios.append(dic)

        for nivel in niveis.values():
            nivelsuperior = nivel['nivelSuperior_id']
            nivelinfeiror = nivel['nivelInferior_id']
            if (nivel['nivelSuperior_id'] == None):
                nivelsuperior = '0'
            if (nivel['nivelInferior_id'] == None):
                nivelinfeiror = '0'
            if (nivel['nivelSuperior_id'] == None and nivel['nivelInferior_id'] == None):
                nivelsuperior = '0'
                nivelinfeiror = '0'

            setoresnivel = Setor.objects.select_related('nivel').filter(
                nivel__organizacao=self.request.user.funcionario.organizacao, nivel__pk=nivel['id'])
            lSetores = []
            for setor in setoresnivel.values():
                funcionarios = Funcionario.objects.filter(setor__pk=setor['id'])
                lfunc = []
                for func in funcionarios:
                    dic = {
                        'id': func.pk
                    }
                    lfunc.append(dic)

                dicSetor1 = {
                    'id': setor['id'],
                    'nome': setor['nome'],
                    'funcionarios': lfunc,
                    'gerente': {'id': setor['gerente_id']}
                }
                lSetores.append(dicSetor1)

            lSocilitacoesDelegacoes = []
            solicitacoes = Solicitacao.objects.prefetch_related('nivel').filter(nivel__id=nivel['id'])
            for solicitacao in solicitacoes:
                ld = []
                for item in solicitacao.itens.values('id', 'nome'):
                    listaCampos = []
                    campos = list(Solicitacao.objects.prefetch_related('itens__campus').filter(itens__campus__item=item['id']).values('itens__campus','itens__campus__descricao','itens__campus__tipo','itens__campus__nome').distinct())
                    for campo in campos:
                        dictCampo = {
                            'id': campo['itens__campus'],
                            'nome': campo['itens__campus__nome'],
                            'descricao': campo['itens__campus__descricao'],
                            'tipo': campo['itens__campus__tipo']
                        }
                        listaCampos.append(dictCampo)
                    dicitensdelegacao = {
                        'id': item['id'],
                        'nome': item['nome'],
                        'tipoCampos': listaCampos
                    }
                    ld.append(dicitensdelegacao)
                dic = {
                    'id': solicitacao.pk,
                    'nome': solicitacao.tipo,
                    'descricao': solicitacao.descricao,
                    'tipo': solicitacao.solicitacaoDelegacao,
                    'tipoItens': ld
                }

                lSocilitacoesDelegacoes.append(dic)

            dic = {
                'id': nivel['id'],
                'nome': nivel['nome'],
                'nivelSuperior': nivelsuperior,
                'nivelInferior': nivelinfeiror,
                'responsavel': {'id': nivel['funcionario_id']},
                'setores': lSetores,
                'tipoSolicitacoesDelegacoes': lSocilitacoesDelegacoes
            }
            lNiveis.append(dic)

        for organizacao in organizacoes:
            organizacaoDic = {
                'id': organizacao['id'],
                'nome': organizacao['nome'],
                'cnpj': organizacao['cnpj'],
                'endereco': organizacao['endereco'],
                'telefone': organizacao['telefone'],
                'situacao': organizacao['situacao'],
                'enviado': True,
                'pedido': organizacao['pedido'],
                'funcionarios': lFuncionarios,
                'niveis': lNiveis,
            }

        lOrganizacao1.append(organizacaoDic)

        # Envio da request
        resp = requests.post(url='http://127.0.0.1:8080/SAPH/saph/organizacao/exportar/',
                             data=json.dumps(lOrganizacao1),
                             headers={'content-type': 'application/json'})
        if (resp.status_code == 200 or resp.status_code == 201):
            org = get_object_or_404(Organizacao, pk=organizacoes[0]['id'])
            org.enviado = True
            org.save()
            return HttpResponse("sim")
        else:
            return HttpResponse("nao")
