from django.urls import (
    path,
    include
)

urlpatterns = [

    path(
        "clientes/",
        include(
            "veterinaria.urls.cliente_urls"
        )
    ),

    path(
        "mascotas/",
        include(
            "veterinaria.urls.mascota_urls"
        )
    ),

    path(
        "veterinarios/",
        include(
            "veterinaria.urls.veterinario_urls"
        )
    ),

    path(
        "citas/",
        include(
            "veterinaria.urls.cita_urls"
        )
    ),

    path(
        "historias-clinicas/",
        include(
            "veterinaria.urls.historia_clinica_urls"
        )
    ),
]