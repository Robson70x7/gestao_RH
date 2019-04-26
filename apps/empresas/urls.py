from django.urls import path
from . import views

app_name = 'empresa'
urlpatterns = [
    path('', views.ListaEmpresas.as_view(), name="listar"),
    path('novo/', views.CriarEmpresa.as_view(), name="criar"),
    path('edit/<int:pk>', views.EditarEmpresa.as_view(), name="editar"),
]