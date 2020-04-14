from django.shortcuts import redirect, render
from .models import Servicio, agendaServicio
from .forms import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from django.core import serializers


# Create your views here.

def home(request):
    return render(request,'luna/index.html')

def servicio(request):
    return render(request,'luna/servicio.html')

def registro(request):   
    data = {
        'form': CustomUser()
    } 
    
    if request.method == 'POST':
        formulario = CustomUser(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            #login user creado
            
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username , password= password)
            login(request, user) 
            
            return redirect(to='home')
            
    return render(request,'registration/registro.html', data)


@login_required
def agendar(request):
    serv = Servicio.objects.all()
    s={'servicio':serv}
    
    if request.POST:
        agenda = agendaServicio()
        agenda.nombre = request.POST.get('txtNombre')
        agenda.apellido = request.POST.get('txtApellido')
        agenda.direccion = request.POST.get('txtDireccion')
        
        serv = Servicio()
        serv.id= request.POST.get('cbService')
        agenda.tipoServicio = serv
        
        try:
            agenda.save()
            messages.success(request, 'Solicitud guardado')
            return redirect(to='home')
        except:
            messages.success(request, 'Error al guardar')
    return render(request,'luna/agendar.html',s)

def profile(request, id):
    if id == 'admin':
       servicio = agendaServicio.objects.all()
       serv = {'servicio':servicio}
    else:
        
        servicio = agendaServicio.objects.filter(nombre = id)
        serv = {'servicio':servicio}

    return render(request,'luna/profile.html',serv)
    

def eliminar_servicio(request, id):
    #busca la id del servicio para borrarlo 
    serv = agendaServicio.objects.get(id=id)

    try:
        serv.delete()
        mensaje = "Servicio eliminado"
        messages.success(request, mensaje)
    except:
        mensaje = "Servicio no eliminado"
        messages.error(request, mensaje)
    
    return redirect(to='home')

def modificar_solicitud(request, id):
    agenda = agendaServicio.objects.get(id=id)
    serv = Servicio.objects.all()
    variables = {
        'agenda':agenda,
        'servicio':serv

    }
    if request.POST:
        agenda = agendaServicio()
        agenda.id = request.POST.get('txtId')
        agenda.nombre = request.POST.get('txtNombre')
        agenda.apellido = request.POST.get('txtApellido')
        agenda.direccion = request.POST.get('txtDireccion')
        
        serv = Servicio()
        serv.id= request.POST.get('cbService')
        agenda.tipoServicio = serv
        
        try:
            agenda.save()
            messages.success(request,'modificado correctamente')
            return redirect(to='home')
        except:
            messages.success(request,'modificado no correctamente')
        return redirect(to='profile')

    return render(request,'luna/modificar.html', variables)