from django.contrib import admin
from django.urls import path, include
from App import views 

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('reset_password', views.reset_password, name='reset'),

    path('', views.listarAcoes),  
    path('adicionar',views.adicionar),  
    path('editar/<int:id>', views.editar),  
    path('atualizar/<int:id>', views.atualizar),  
    path('remover/<int:id>', views.remover),

    path('api/v1/', include('api.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
