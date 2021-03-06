from django.db import models
from django.contrib.auth.models import User
from apps.departamentos import models as dept_model
from apps.empresas.models import Empresa

class Funcionario(models.Model):
    nome = models.CharField(max_length=70)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    departamento = models.ManyToManyField(dept_model.Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('funcionarios:home')

    def __str__(self):
        return self.nome
