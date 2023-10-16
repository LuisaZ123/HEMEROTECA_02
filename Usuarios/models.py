from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class user(AbstractUser):
    REQUIRED_FIELDS= ["email"]

class autor (models.Model):
    nombre = models.CharField('Nombre', max_length=40, blank=True)
    fecha_de_nacimiento=models.DateField()



