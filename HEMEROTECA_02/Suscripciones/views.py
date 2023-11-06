from django.shortcuts import render
from rest_framework.viewsets import viewset, ModelViewset
from .serializers import SuscripciónSerializer
from .models import suscripción

# Create your views here.
class CreatePermision(BasePermission):
    def has_permission(self, request, view):
        print(f"Pase por el permiso {request.user.id}")
        if view.action == "create" : return request.user.rol == 1,2,6
        return True
class prestamoViewset(viewset):
    serializer_class= SuscripciónSerializer 
    queryset = suscripción.objects.all()


