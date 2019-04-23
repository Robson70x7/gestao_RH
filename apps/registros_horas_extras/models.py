from django.db import models

class RegistroHoraExtra(models.Model):

    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'RegistroHoraExtra'
        verbose_name_plural = 'Registros Horas Extras'

    def __str__(self):
        return self.nome
