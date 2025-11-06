from django import forms
from .models import Turno, Reseña

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ["cliente", "servicio", "fecha_hora"]
        widgets = {
    "fecha_hora": forms.DateTimeInput(attrs={"type": "datetime-local"})
}


class ResenaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ["autor", "texto"]

