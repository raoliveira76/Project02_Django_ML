from socket import fromshare
from django import forms
from genero.models import GeneroModel


class GeneroForm(forms.Form):
	# def __init__(self, *args, **kwargs):
	# 	super(GeneroForm, self).__init__(*args, **kwargs)

	# 	self.fields['descricao'].error_messages = {"required": "Campo Obritagório"}
		
	# descricao = forms.CharField(label='Gênero', required=True)

	class Meta:
		model = GeneroModel
		fields = '__all__'