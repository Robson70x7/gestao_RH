from django.db import models
from apps.funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):

    motivo_hora_extra = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'RegistroHoraExtra'
        verbose_name_plural = 'Registros Horas Extras'

    def __str__(self):
        return self.funcionario
