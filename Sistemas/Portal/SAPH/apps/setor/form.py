from django.forms import ModelForm

from apps.funcionario.models import Funcionario
from apps.nivel.models import Nivel
from .models import Setor


class SetorCreate(ModelForm):
    def __init__(self, organizacao, *args, **kwargs):
        funcionarios = Funcionario.objects.filter(organizacao=organizacao, ativo=True)
        niveis= Nivel.objects.filter(organizacao=organizacao)
        super(SetorCreate, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = funcionarios
        self.fields['nivel'].queryset = niveis
        self.fields['gerente'].queryset = funcionarios

        self.fields['funcionario'].widget.attrs = {'class' : 'custom-select'}
        self.fields['nivel'].widget.attrs = {'class' : 'custom-select custom-select-sm'}
        self.fields['gerente'].widget.attrs = {'class' : 'custom-select custom-select-sm'}

    class Meta:
        model = Setor
        fields = ['nome','funcionario', 'nivel', 'gerente']
