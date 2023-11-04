from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import formCliente, formMedico,formContacti
from .models import Cliente, medico,contacto
from django.contrib.auth.decorators import user_passes_test

def gestion(request): # primera vista
    
    return render(request,'usuarios/menuAdmin.html')


def saludo(request): # primera vista

    return render(request,'usuarios/index.html')

def servicios(request): # primera vista

    return render(request,'usuarios/servicios.html')

def nosotros(request): # primera vista

    return render(request,'usuarios/nosotros.html')

def saludo2(request): # primera vista

    return render(request,'usuarios/inicio.html')

def registroContacto(request): 

    data={
        'form': formContacti()
    }
    if request.method =='POST':
        formulario2 = formContacti(data=request.POST)

        if formulario2.is_valid():
                formulario2.save()
                data["mensaje"] = "1 contacte formulario: ContactoForm"
        else:
            data["form"] = formulario2
    return render(request,'usuarios/contactanos.html',data)



def resgistroPaciente(request): 

    data={
        'formu': formCliente()
    }
    if request.method =='POST':
        formulario = formCliente(data=request.POST, files=request.FILES)

        if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "1 contacte formulario: ContactoForm"
        else:
            data["formu"] = formulario
    

    return render(request,'usuarios/formulario1.html',data)


def resgistroMedico(request): 

    data={
        'form': formMedico()
    }
    if request.method =='POST':
        formulario2 = formMedico(data=request.POST)

        if formulario2.is_valid():
                formulario2.save()
                data["mensaje"] = "1 contacte formulario: ContactoForm"
        else:
            data["form"] = formulario2
    

    return render(request,'usuarios/formulario2.html',data)



def modificar(request): 
    campo1=None
    if request.method == 'POST':
        campo1 = request.POST.get('campo1')
        personas = Cliente.objects.filter(DPI=campo1)
    else:
        personas = Cliente.objects.all()
    data={
        'persona':personas
    }

    return render(request, 'usuarios/modificar.html',data)


def modificar2(request, id):
    clien = get_object_or_404(Cliente, id=id)
    data = {
        'form': formCliente(instance=clien)
    }

    if request.method == 'POST':
        formu= formCliente(data=request.POST, instance=clien, files=request.FILES)
        if formu.is_valid:
            formu.save()
            return redirect(to="modifi")
        else:
            data["form"] = formu

    return render(request, 'usuarios/modificar2.html', data)


def elimindarcli(request, id):
    clien = get_object_or_404(Cliente, id=id)
    clien.delete()
    return redirect(to="modifi")


def modificarMedico(request): 
    campo1=None
    if request.method == 'POST':
        campo1 = request.POST.get('campo2')
        personal = medico.objects.filter(Nombre=campo1)
    else:
        personal = medico.objects.all()
    
    data={
        'medico1':personal
    }

    return render(request, 'usuarios/modificarMedico.html',data)


def modificarMedico2(request, id):
    producto = get_object_or_404(medico, id=id)
    data = {
        'form': formMedico(instance=producto)
    }

    if request.method == 'POST':
        formu= formMedico(data=request.POST, instance=producto, files=request.FILES)
        if formu.is_valid:
            formu.save()
            return redirect(to="modifiMe")
        else:
            data["form"] = formu

    return render(request, 'usuarios/modificarMedico2.html', data)


def elimindarcli(request, id):
    med = get_object_or_404(medico, id=id)
    med.delete()
    return redirect(to="modifiMe")

