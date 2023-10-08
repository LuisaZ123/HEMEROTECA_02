from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class user(AbstractUser):
    REQUIRED_FIELDS= ["email"]

class suscripción(models.Model):
    user = models.ForeignKey("user", on_delete=models.CASCADE)
    fecha_de_inicio= models.DateTimeField()
    fecha_de_salidas= models.DateTimeField()

class autor (models.Model):
    nombre = models.CharField('Nombre', max_length=40, blank=True)
    fecha_de_nacimiento=models.DateField()



