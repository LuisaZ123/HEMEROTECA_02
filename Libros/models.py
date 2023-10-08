from django.db import models
from Libros.models import autor

# Create your models here.
class libro(models.Model):
    nombre = models.CharField('Nombre', max_length=320, null = False, blank= False )
    edición = models.IntegerField()
    autor = models.ForeignKey('autor', on_delete=models.CASCADE)
    fecha_de_publicación= models.DateTimeField()

class copy(models.Model):
    state = models.CharField(max_length=100)
    libro= models.ForeignKey(libro, on_delete=models.DO_NOTHING, null=False, blank=False)
    ubicación =models.CharField(max_length=100)

class publicación(models.Model):
    fecha = models.DateField()
    frecuencia = models.IntegerField()
