from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Cliente(models.Model):
    nombre = models.CharField(max_length=80)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    duracion_minutos = models.PositiveIntegerField(
        validators=[MinValueValidator(5)]
    )

    def __str__(self):
        return f"{self.nombre} - {self.duracion_minutos} min"


class Turno(models.Model):
    ESTADOS = [
        ("PEND", "Pendiente"),
        ("CONF", "Confirmado"),
        ("CANC", "Cancelado"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=4, choices=ESTADOS, default="PEND")

    class Meta:
        ordering = ["-fecha_hora"]

    def __str__(self):
        fecha = timezone.localtime(self.fecha_hora).strftime("%d/%m %H:%M")
        return f"{fecha} - {self.cliente} - {self.servicio}"


class Reseña(models.Model):
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, related_name="reseñas")
    autor = models.CharField(max_length=50)
    texto = models.TextField(max_length=300)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"Reseña de {self.autor} - {self.turno}"
