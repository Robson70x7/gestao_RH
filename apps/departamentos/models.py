from django.db import models
from apps.empresas.models import Empresa


class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ('-nome',)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('departamentos:home')

    def __str__(self):
        return self.nome
