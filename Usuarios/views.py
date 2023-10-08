from django.shortcuts import render
from rest_framework.viewsets import viewset, ModelViewset
from .serializers import userSerializer
from .models import user

# Create your views here.
class userViewset(viewset):
    serializer_class= userSerializer
    queryset = user.objects.all()
# Create your views here.
