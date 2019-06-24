import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from pip._vendor import requests

from apps.funcionario.models import Funcionario
from apps.nivel.models import Nivel
from apps.item.models import Item
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
				# 'foto': funcionario.foto,
				'foto': "Foto",
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
			solicitacoes = Solicitacao.objects.prefetch_related('nivel').filter(nivel__id=nivel['id'])
			lSocilitacoes = []
			for solicitacao in solicitacoes:
				lisa = []
				for sol in solicitacao.itens.values('id', 'nome'):
				# for sol in solicitacao.itens:
					# solicitacao.itens.prefetch_related('campus')[0]
					# Item.objects.prefetch_related('campus')[0].campus.values()
					# Item.objects.prefetch_related('campus').filter(campus__pk=1)
					# FALTA ISSO AQUI
					listacampus = []
					for campus in Item.objects.prefetch_related('campus').all():
						listacampus.append(campus)

					dicitenssolicitacao = {
						'id': sol['id'],
						'nome': sol['nome'],
						'tipoCampos': listacampus
					}
					lisa.append(dicitenssolicitacao)
				dic = {
					'id': solicitacao.pk,
					'nome': solicitacao.tipo,
					'descricao': solicitacao.descricao,
					'tipo': 'SOLICITACAO',
					'tipoItens': lisa
				}

				lSocilitacoes.append(dic)

			dic = {
				'id': nivel['id'],
				'nome': nivel['nome'],
				'nivelSuperior': nivelsuperior,
				'nivelInferior': nivelinfeiror,
				'responsavel': {'id': nivel['funcionario_id']},
				'setores': lSetores,
				'tipoSolicitacoesDelegacoes': lSocilitacoes
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
				'funcionarios': lFuncionarios,
				'niveis': lNiveis,
			}

		lOrganizacao1.append(organizacaoDic)

		# Envio das requests
		# resp = requests.post(url='http://localhost:8080/SAPH/saph/organizacao/exportar/',
		# 							data=json.dumps(lOrganizacao1),
		# 							headers={'content-type': 'application/json'})
		# if (resp.status_code == 200 or resp.status_code == 201):
		# 	return HttpResponse("sim")
		# else:
		# 	return HttpResponse("nao")
		a = 10