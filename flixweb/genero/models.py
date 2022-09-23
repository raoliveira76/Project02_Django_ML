from django.db import models


class GeneroModel(models.Model):
	descricao = models.CharField(max_length=50)

	def __str__(self) -> str:
		return self.descricao
