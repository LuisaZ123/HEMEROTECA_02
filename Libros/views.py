from django.shortcuts import render
from rest_framework.viewsets import viewset, ModelViewset
from .serializers import libroSerializer
from .models import libro

class CreatePermision(BasePermission):
    def has_permission(self, request, view):
        print(f"Pase por el permiso {request.user.id}")
        if view.action == "create" : return request.user.rol == 1,2,3,4,5,6
        return True
# Create your views here.
class libroViewset(viewset):
    serializer_class= libroSerializer
    queryset = libro.objects.all()
