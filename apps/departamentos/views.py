from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Departamento

class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        depatamento = form.save(commit=False)
        empresa_logada = self.request.user.funcionario.empresa
        depatamento.empresa = empresa_logada
        depatamento.save()
        return super(DepartamentoCreate, self).form_valid(form)


class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = ['nome']


class DepartamentoList(ListView):
    model = Departamento
    context_object_name = 'departamentos'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoDelete(DeleteView):
    model = Departamento
    from django.urls import reverse_lazy
    success_url = reverse_lazy('departamentos:home')


class DepartamentoDetalhe(DetailView):
    pass

