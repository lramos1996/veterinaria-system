from django.urls import (
    path,
    include
)

urlpatterns = [
    path(
        "productos/",
        include(
            "inventario.urls.producto_urls"
        )
    ),
    
    path(
        "categorias-productos/",
        include(
            "inventario.urls.categoria_producto_urls"
        )
    ),

    path(
        "movimientos/",
        include(
            "inventario.urls.movimientos_url"
        )
    ),
   
   path(
        "kardex/",
        include(
            "inventario.urls.kardex_url"
        )
    ),

    path(
        "proveedores/",
        include(
            "inventario.urls.proveedor_urls"
        )
    ),

    path(
    "compras/",
    include(
        "inventario.urls.compra_urls"
    )
),
]