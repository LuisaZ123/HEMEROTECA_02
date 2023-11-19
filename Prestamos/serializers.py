from rest_framework import serializers
from .models import prestamo
class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model= prestamo
        fields = "__all__"

