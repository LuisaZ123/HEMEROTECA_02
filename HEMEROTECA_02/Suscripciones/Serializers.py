from rest_framework import serializers
from .models import suscripción
class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model= suscripción
        fields = "__all__"