from django.contrib import admin

from veterinaria.models import (
    Cliente,
    Mascota,
    Veterinario,
    Cita,
    HistoriaClinica
)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nombres",
        "apellidos",
        "documento",
        "telefono"
    )

    search_fields = (
        "nombres",
        "apellidos",
        "documento"
    )


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nombre",
        "especie",
        "raza",
        "propietario"
    )

    search_fields = (
        "nombre",
        "raza"
    )

    list_filter = (
        "especie",
        "sexo"
    )


@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nombres",
        "apellidos",
        "especialidad",
        "activo"
    )

    search_fields = (
        "nombres",
        "apellidos",
        "colegiatura"
    )


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "mascota",
        "veterinario",
        "fecha",
        "hora",
        "estado"
    )

    list_filter = (
        "estado",
        "fecha"
    )


@admin.register(HistoriaClinica)
class HistoriaClinicaAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "mascota",
        "veterinario",
        "fecha_atencion"
    )

    search_fields = (
        "mascota__nombre",
        "diagnostico"
    )

    list_filter = (
        "fecha_atencion",
    )