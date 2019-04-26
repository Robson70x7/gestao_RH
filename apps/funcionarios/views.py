from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView, DeleteView
from . import models


class FuncionariosList(ListView):
    model = models.Funcionario
    context_object_name = 'funcionarios'
    
    def get_queryset(self):
        empresa = self.request.user.funcionario.empresa
        return models.Funcionario.objects.filter(empresa=empresa)


class FuncionarioUpdate(UpdateView):
    model = models.Funcionario
    fields = '__all__'


class FuncionarioDetalhe(DetailView):
    model = models.Funcionario
    context_object_name = 'funcionario'

class FuncionarioDelete(DeleteView):
    model = models.Funcionario
    from django.urls import reverse_lazy
    success_url = reverse_lazy('funcionarios:home')