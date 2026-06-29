from django.urls import (
    path,
    include
)

urlpatterns = [
    path(
        "tipos-comprobante/",
        include(
            "facturacion.urls.tipo_comprobante_urls"
        )
    ),

    path(
        "metodos-pago/",
        include(
            "facturacion.urls.metodo_pago_urls"
        )
    ),

    path(
        "ordenes-servicio/",
        include(
            "facturacion.urls.orden_servicio_urls"
        )
    ),

    path(
        "detalles-orden-servicio/",
        include(
            "facturacion.urls.detalle_orden_servicio_urls"
        )
    ),

    path(
        "comprobantes/",
        include(
            "facturacion.urls.comprobante_urls"
        )
    ),

    path(
        "movimientos-caja/",
        include(
            "facturacion.urls.movimiento_caja_urls"
        )
    ),
]