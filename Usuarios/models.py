from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class user(AbstractUser):
    ROLES_HEMEROTECA: (
        1, "BIBLIOTECARIO",
        2,"ARCHIVISTA",
        3, "INVESTIGADOR",
        4, "ESTUDIANTE", 
        5, "LECTOR",
        6, "ADMINISTRADOR"
    )
    REQUIRED_FIELDS= ["email"]
    rol = models.IntegerField(choices=ROLES_HEMEROTECA)

class autor (models.Model):
    nombre = models.CharField('Nombre', max_length=40, blank=True)
    fecha_de_nacimiento=models.DateField()



