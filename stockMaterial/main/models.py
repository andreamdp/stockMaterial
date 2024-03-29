# -*- encoding: utf-8 -*-
from django.db import models
from datetime import date

class Proveedor(models.Model):
	codigo =models.CharField('Código',max_length=32, unique=True)
	nombre=models.CharField(max_length=200)
	telefono=models.CharField(max_length=200, null=True, blank= True)
	direccion= models.CharField(max_length=200, null=True, blank= True)
	mail=models.CharField(max_length=50,null=True, blank= True)
class Cliente(models.Model):
    codigo = models.CharField('Código',max_length=32, unique=True)
    nombre = models.CharField(max_length=64)
    telefono = models.CharField('Teléfono',max_length=100)
    direccion = models.CharField('Dirección',max_length=100)
    mail = models.CharField('E-mail',max_length=100)
class Presupuesto(models.Model):
	cliente = models.ForeignKey('Cliente')
	#producto = models.ForeignKey('Producto')
	descripcion = models.CharField(max_length=8000)
class Producto(models.Model):
    codigo = models.CharField('Código',max_length=32, unique=True)
    nombre = models.CharField(max_length=64)
    precioCosto = models.FloatField( 'Costo',null=True, blank=True)
    precioVta = models.FloatField('Precio de Venta',null=True, blank=True)
    qty = models.PositiveIntegerField(default=0)
    proveedor= models.ForeignKey('Proveedor')
    presupuesto= models.ForeignKey('Presupuesto')
    def update_qty(self, qty):
        """ creates a movement with the diff """
        mov, _ = Movimiento.objects.get_or_create(producto=self, dia=date.today())
        mov.qty += qty - self.qty
        mov.save()
        self.qty = qty
        self.save()

    def qty_on(self, day):
        """ returns qty on specific day """
        return self.qty - sum(
            Movimiento.objects.filter(producto=self, day__range=(dia,
                date.today())).values_list('qty', flat=True))
class Movimiento(models.Model):
    producto = models.ForeignKey(Producto)
    dia = models.DateField(default=date.today())
    qty = models.IntegerField(default=0)

    class Meta:
        unique_together = ('producto', 'dia')
