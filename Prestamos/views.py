from django.shortcuts import render
from rest_framework.viewsets import viewset, ModelViewset
from .serializers import prestamoSerializer
from .models import prestamo

# Create your views here.
class prestamoViewset(viewset):
    serializer_class= prestamoSerializer
    queryset = prestamo.objects.all()
