from django.shortcuts import render
from rest_framework.viewsets import viewset, ModelViewset
from .serializers import libroSerializer
from .models import libro

# Create your views here.
class libroViewset(viewset):
    serializer_class= libroSerializer
    queryset = libro.objects.all()
