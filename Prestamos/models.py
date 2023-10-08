from django.db import models

from Usuarios.models import AbstractUser
from Libros.models import copy
from Libros.models import libro
# Create your models here.
class prestamo(models.Model):
    id_prestamo = models.AutoField('ID', primary_key=True)
    user = models.ForeignKey("usuarios", on_delete=models.CASCADE, verbose_name="Usuario")
    libro = models.ForeignKey("libro", on_delete=models.SET_NULL, null=True, blank=True)
    copy = models.ForeignKey(copy, on_delete=models.DO_NOTHING)