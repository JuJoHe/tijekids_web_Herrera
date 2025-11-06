from django.shortcuts import render, redirect, get_object_or_404
from .forms import TurnoForm, ResenaForm
from .models import Turno, Reseña
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request, "turnos/home.html")

@login_required
def crear_turno(request):
    if request.method == "POST":
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ver_turnos")   # tras crear, ir al listado
    else:
        form = TurnoForm()
    return render(request, "turnos/crear_turno.html", {"form": form})


@login_required
def ver_turnos(request):
    turnos = Turno.objects.all().order_by("-fecha_hora")
    return render(request, "turnos/ver_turnos.html", {"turnos": turnos})

@login_required
def crear_resena(request, turno_id):
    turno = Turno.objects.get(id=turno_id)
    if request.method == "POST":
        form = ResenaForm(request.POST)
        if form.is_valid():
            reseña = form.save(commit=False)
            reseña.turno = turno
            reseña.save()
            return redirect("detalle_turno", turno_id=turno.id)  # volver al detalle
    else:
        form = ResenaForm()
    return render(request, "turnos/crear_resena.html", {"form": form, "turno": turno})



def ver_resenas(request):
    resenas = Reseña.objects.all()
    return render(request, "turnos/ver_resenas.html", {"resenas": resenas})


def detalle_turno(request, turno_id):
    turno = Turno.objects.get(id=turno_id)
    resenas = turno.reseñas.all()
    return render(request, "turnos/detalle_turno.html", {"turno": turno, "resenas": resenas})

def eliminar_turno(request, id):
    turno = get_object_or_404(Turno, id=id)
    turno.delete()
    return redirect('ver_turnos')

def eliminar_resena(request, resena_id):
    resena = get_object_or_404(Reseña, id=resena_id)
    resena.delete()
    return redirect('ver_resenas')


