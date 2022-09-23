from asyncio.windows_events import NULL
from django.shortcuts import render

from pathlib import Path


def index(request):
	return render(request, "principal/index.html")

