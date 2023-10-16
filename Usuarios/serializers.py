from rest_framework import serializers
from .models import user, suscripción

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model= user
        fields = "__all__"
class SuscripciónSerializer(serializers.ModelSerializer):
    class Meta:
        model= suscripción 
        fields = "__all__"