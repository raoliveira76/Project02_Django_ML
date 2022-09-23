from asyncio.windows_events import NULL
from django.shortcuts import render
from . import forms


def cadastro(request):
	form = forms.GeneroForm()
	data_dict = {'form_genero': form}

	return render(request, "genero/genero.html", data_dict)

