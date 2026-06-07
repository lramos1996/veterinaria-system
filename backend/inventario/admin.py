from django.contrib import admin

from .models import CategoriaProducto
from .models import Proveedor
from .models import Producto
from .models import MovimientoInventario
from .models import Kardex

admin.site.register(CategoriaProducto)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(MovimientoInventario)
admin.site.register(Kardex)