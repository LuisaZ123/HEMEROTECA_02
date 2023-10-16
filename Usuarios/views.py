from django.shortcuts import render
from rest_framework.viewsets import viewset, ModelViewset
from rest_framework.response import Response
from .serializers import UserSerializer, SuscripciónSerializer
from .models import user, suscripción

# Create your views here.
class userViewset(viewset):
    serializer_class= UserSerializer
    queryset = user.objects.all()

class SuscriciónViewset(viewset):
    serializer_class= SuscripciónSerializer
    queryset = suscripción.objects.all()

def create(self, request, *args, **kwargs):

    serializer =  self.get_serializer(data= request.data)
    serializer.is_valid(raise_exception= True)
    
    data = serializer.data

    _suscripción= suscripción.objects.filter(user_id = data.get ("user"), start_date__lt= data.get("end_date"), end_date__gt= data.get("start_date"))
    if len(_suscripción)>0:
        raise Exception("Ya existe una suscripción")

    return Response({"status": "created"}):
