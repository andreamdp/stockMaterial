from django.contrib import admin
from models import *

class ProductoInline(admin.TabularInline):
    model = Producto
    def get_extra(self, request, obj=None, **kwargs):
        extra =0
        if obj:
            return extra - obj.binarytree_set.count()
        return extra
class PresupuestoAdmin(admin.ModelAdmin):
    inlines = [
        ProductoInline,
    ]


admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Presupuesto,PresupuestoAdmin)
admin.site.register(Producto)
admin.site.register(Movimiento)
