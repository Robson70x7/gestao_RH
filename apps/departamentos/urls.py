from django.urls import path
from . import views

app_name = 'departamentos'
urlpatterns = [
    path('', views.DepartamentoList.as_view(), name='home'),
    path('novo/', views.DepartamentoCreate.as_view(), name='novo'),
    path('editar/<int:pk>/', views.DepartamentoUpdate.as_view(), name='editar'),
    path('excluir/<int:pk>/', views.DepartamentoDelete.as_view(), name='excluir'),
]
