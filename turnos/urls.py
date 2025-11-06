from django.urls import path
from . import views

urlpatterns = [
    path("", views.ver_turnos, name="ver_turnos"),
    path("crear-turno/", views.crear_turno, name="crear_turno"),
    path("ver-resenas/", views.ver_resenas, name="ver_resenas"),
    path("crear-resena/<int:turno_id>/", views.crear_resena, name="crear_resena"),
    path("turno/<int:turno_id>/", views.detalle_turno, name="detalle_turno"),
    path('ver-turnos/', views.ver_turnos, name='ver_turnos'),
    path('eliminar-turno/<int:id>/', views.eliminar_turno, name='eliminar_turno'),
    path("resena/<int:resena_id>/eliminar/", views.eliminar_resena, name="eliminar_resena"),

]
