from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Project, Experiencia, Educacion
from .forms import EducacionForm
from django.contrib.auth.decorators import login_required



@login_required
def home(request):
    projects = Project.objects.all()
    experiencia = Experiencia.objects.all()
    return render(request, "home.html", {
        "projects": projects,
        "experiencias": experiencia
        })

def registrar(request):
    if request.method == 'GET':
        return render(request, "registrar.html", {
            'form': UserCreationForm
        })
    else: 
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(request, "registrar.html", {
                    'form': UserCreationForm,
                    "error": "El nombre de usuario ya ha sido tomado. Por favor, elige otro nombre."
                    })
        else:
            return render(request, "registrar.html", {
                'form': UserCreationForm,
                "error": "Las contraseñas no coinciden."
                })
        
def cerrarSeccion(request):
    logout(request)
    return redirect('home')


def iniciarSeccion(request):
    if request.method == 'GET':
        return render(request, "InicioDeSeccion.html", {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "InicioDeSeccion.html", {
                'form': AuthenticationForm,
                "error": "Nombre de usuario y/o contraseña incorrectos."
            })
        else:
            login(request, user)
            return redirect("home")


@login_required
def educacion_list(request):
    educaciones = Educacion.objects.all()
    return render(request, 'educacion_list.html', {'educaciones': educaciones})

@login_required
def educacion_create(request):
    if request.method == 'POST':
        form = EducacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('educacion_list')
    else:
        form = EducacionForm()
    return render(request, 'educacion_form.html', {'form': form})

@login_required
def educacion_update(request, pk):
    educacion = get_object_or_404(Educacion, pk=pk)
    if request.method == 'POST':
        form = EducacionForm(request.POST, instance=educacion)
        if form.is_valid():
            form.save()
            return redirect('educacion_list')
    else:
        form = EducacionForm(instance=educacion)
    return render(request, 'educacion_form.html', {'form': form})

@login_required
def educacion_delete(request, pk):
    educacion = get_object_or_404(Educacion, pk=pk)
    if request.method == 'POST':
        educacion.delete()
        return redirect('educacion_list')
    return render(request, 'educacion_confirm_delete.html', {'educacion': educacion})