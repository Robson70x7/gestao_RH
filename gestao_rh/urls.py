from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls

urlpatterns = [
    path('', include('apps.core.urls', namespace='core')),
    path('funcionarios/', include('apps.funcionarios.urls', namespace='funcionarios')),
    path('empresa/', include('apps.empresas.urls', namespace='empresa')),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
