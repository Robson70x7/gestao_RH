from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from django.contrib.auth.models import User
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

class FuncionarioCreate(CreateView):
    model = models.Funcionario
    fields = ['nome', 'departamento']
    context_object_name = 'funcionario'

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        
        # Criando username e senha
        f_split = funcionario.nome.split()
        username = str('.'.join([f_split[0], f_split[-1]])).lower()
        password = ''.join([f_split[0].title() , '122570'])

        funcionario.user_id = User.objects.create_user(username=username, password=password)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)