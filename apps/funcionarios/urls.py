from django.urls import path
from . import views


app_name = 'funcionarios'
urlpatterns = [
    path('', views.FuncionariosList.as_view(), name='home'),
    path('editar/<int:pk>/', views.FuncionarioUpdate.as_view(), name='atualizar'),
    path('detalhe/<int:pk>/', views.FuncionarioDetalhe.as_view(), name='detalhe'),
    path('excluir/<int:pk>/', views.FuncionarioDelete.as_view(), name='excluir'),
]