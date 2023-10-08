from rest_framework import serializers
from .models import libro
class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model= libro
        fields = "__all__"


