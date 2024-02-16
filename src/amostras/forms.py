from django import forms
from .models import Amostra

class AmostraForm(forms.ModelForm):
    class Meta:
        model = Amostra
        fields = ['nome', 'descricao', 'quantidade_solucao']