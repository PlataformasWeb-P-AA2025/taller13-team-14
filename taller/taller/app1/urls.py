"""
URL configuration for taller project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from app1 import views
from rest_framework import routers
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'edificios', views.EdificioViewSet)
router.register(r'departamentos', views.DepartamentoViewSet)


urlpatterns = [
        path('', views.index, name='index'),
        path('api/', include(router.urls)),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('edificios/listar/', views.listar_edificios, name='listar_edificios'),
        path('departamentos/listar/', views.listar_departamentos, name='listar_departamentos'),
        path('edificios/crear/', views.crear_edificio, name='crear_edificio'),
        path('departamentos/crear/', views.crear_departamento, name='crear_departamento'),
        path('entrando/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
        
        path('edificios/editar/<int:pk>/', views.editar_edificio, name='editar_edificio'),
        path('edificios/eliminar/<int:pk>/', views.eliminar_edificio, name='eliminar_edificio'),

        path('departamentos/editar/<int:pk>/', views.editar_departamento, name='editar_departamento'),
        path('departamentos/eliminar/<int:pk>/', views.eliminar_departamento, name='eliminar_departamento'),
]
