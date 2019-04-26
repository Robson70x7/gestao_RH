from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.urls import reverse
from django.http import HttpResponse
from . import models

class CriarEmpresa(CreateView):
    model = models.Empresa
    fields = ['nome']
    success_url = 'core:home'

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('OK')


class EditarEmpresa(UpdateView):
    model = models.Empresa
    fields = ('__all__')
    success_url = '/'


class ListaEmpresas(ListView):
    model = models.Empresa
    template_name = 'empresas/listar_empresa.html'
    context_object_name = 'empresas'
