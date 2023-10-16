from django.db import models

# Create your models here.
class suscripción(models.Model):
    user = models.ForeignKey("user", on_delete=models.CASCADE)
    fecha_de_inicio= models.DateTimeField()
    fecha_de_salidas= models.DateTimeField()
