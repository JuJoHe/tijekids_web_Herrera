
from django.shortcuts import render, redirect
from django import forms

# Create your views here.

# --- (A) Formulario de contacto (simple) ---
class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=80, label="Nombre")
    email = forms.EmailField(label="Email", required=False)
    mensaje = forms.CharField(widget=forms.Textarea, label="Mensaje")

def home(request):
    return render(request, "paginas/home.html")

def about(request):
    return render(request, "paginas/about.html")

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            return render(request, "paginas/contacto_exito.html", {"data": form.cleaned_data})
    else:
        form = ContactoForm()

    return render(request, "paginas/contacto.html", {"form": form})
