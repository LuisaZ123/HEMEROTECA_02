from django.shortcuts import render
from rest_framework.viewsets import viewset, ModelViewset
from .serializers import SuscripciónSerializer
from .models import suscripción

# Create your views here.
class prestamoViewset(viewset):
    serializer_class= SuscripciónSerializer 
    queryset = suscripción.objects.all()

