from django.contrib import admin

from .models import TipoComprobante
from .models import OrdenServicio
from .models import Comprobante
from .models import DetalleComprobante
from .models import MetodoPago
from .models import MovimientoCaja

admin.site.register(TipoComprobante)
admin.site.register(OrdenServicio)
admin.site.register(Comprobante)
admin.site.register(DetalleComprobante)
admin.site.register(MetodoPago)
admin.site.register(MovimientoCaja)