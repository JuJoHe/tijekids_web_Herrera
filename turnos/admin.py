from django.contrib import admin
from .models import Cliente, Servicio, Turno

# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono", "email")
    search_fields = ("nombre", "telefono", "email")


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "duracion_minutos")
    search_fields = ("nombre",)


@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ("fecha_hora", "cliente", "servicio", "estado")
    list_filter = ("estado", "servicio")
    search_fields = ("cliente__nombre", "servicio__nombre", "notas")
