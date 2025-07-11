from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets, permissions
from app1.models import Edificio, Departamento
from app1.serializers import UserSerializer, GroupSerializer, EdificioSerializer, DepartamentoSerializer
from app1.forms import EdificioForm, DepartamentoForm

# Vista normal
def index(request):
    context = {}
    return render(request, 'index.html', context)

def listar_edificios(request):
    edificios = Edificio.objects.all()
    contexto = {
        'edificios': edificios,
        'numero_edificios': edificios.count()
    }
    return render(request, 'listar_edificios.html', contexto)

def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    contexto = {
        'departamentos': departamentos,
        'numero_departamentos': departamentos.count()
    }
    return render(request, 'listar_departamentos.html', contexto)

@login_required(login_url='/entrando/login/')
@permission_required('app1.add_edificio', login_url='/entrando/login/')
def crear_edificio(request):
    if request.method == 'POST':
        form = EdificioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_edificios')
    else:
        form = EdificioForm()
    return render(request, 'crear_edificio.html', {'form': form})

@login_required(login_url='/entrando/login/')
@permission_required('app1.add_departamento', login_url='/entrando/login/')
def crear_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_departamentos')
    else:
        form = DepartamentoForm()
    return render(request, 'crear_departamento.html', {'form': form})

@login_required(login_url='/entrando/login/')
@permission_required('app1.change_edificio', login_url="/entrando/login/")
def editar_edificio(request, pk):
    edificio = Edificio.objects.get(pk=pk)
    if request.method == 'POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_edificios')
    else:
        formulario = EdificioForm(instance=edificio)
    diccionario = {'formulario': formulario}
    return render(request, 'editar_edificio.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('app1.delete_edificio', login_url="/entrando/login/")
def eliminar_edificio(request, pk):
    edificio = Edificio.objects.get(pk=pk)
    edificio.delete()
    return redirect('listar_edificios')

@login_required(login_url='/entrando/login/')
@permission_required('app1.change_departamento', login_url="/entrando/login/")
def editar_departamento(request, pk):
    """
    Edita un registro existente de Departamento.
    """
    departamento = Departamento.objects.get(pk=pk)
    if request.method == 'POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_departamentos')
    else:
        formulario = DepartamentoForm(instance=departamento)
        
    diccionario = {'formulario': formulario}
    return render(request, 'editar_departamento.html', diccionario)

@login_required(login_url='/entrando/login/')
@permission_required('app1.delete_departamento', login_url="/entrando/login/")
def eliminar_departamento(request, pk):
    """
    Elimina un registro de Departamento directamente.
    """
    departamento = Departamento.objects.get(pk=pk)
    departamento.delete()
    return redirect('listar_departamentos')
# Vistas tipo API
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class EdificioViewSet(viewsets.ModelViewSet):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    permission_classes = [permissions.IsAuthenticated]

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
