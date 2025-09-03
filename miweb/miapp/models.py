from django.db import models

# Create your models here.


class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_lenght=5)
    cli_nombre = models.CharField(max_lenght=40, null= True, blank=True)
    cli_direccion = models.CharField(max_lenght= 60, null=True, blank=True)
    cli_telefono=models.CharField(max_lenght=24, null=True, blank=True)

#Agregaremos la tabla en la base de datos
class Meta:
    db_table='CLIENTE'

def __str__(self):
    return self.cli_nombre or f"Cliente{self.id_cliente}"


class Orden(models.Model):
    id_orden=models.AutoField(primary_key=True)
    id_cliente=models.ForeignKey('Cliente', on_delete=models.cascade, to_field='id_cliente')
    ord_fecha = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'ORDEN'

    def __str__(self):
        return f"Orden{self.id_orden}"
    