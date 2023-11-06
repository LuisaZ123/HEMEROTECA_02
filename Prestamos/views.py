from django.shortcuts import render
from rest_framework.viewsets import viewset, ModelViewset
from rest_framework.response import Response
from .serializers import prestamoSerializer
from .models import prestamo

# Create your views here.
class CreatePermision(BasePermission):
    def has_permission(self, request, view):
        print(f"Pase por el permiso {request.user.id}")
        if view.action == "create" : return request.user.rol == 1,6
        return True
class prestamoViewset(viewset):
    serializer_class= prestamoSerializer
    queryset = prestamo.objects.all()

def get_absolute_url(self):
        return Response('prestamo-detail', kwargs={'pk': self.pk})

def is_late(self):
        if self.fecha_de_devolución is None:
            return False
        return self.fecha_de_devolución > self.fecha_de_vencimiento

def get_debt_collection_metric(prestamos):
    total_amount_owed = 0
    for prestamo in prestamos:
        if prestamo.is_late():
            total_amount_owed += prestamo.amount_owed
    return total_amount_owed
