from rest_framework import serializers
from .models import user, suscripción

class UserSerializer(serializers.ModelSerializer):
    password= serializers.Chartfield(write_only= True)

    def create(self, validated_data):
        
        _user = user.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
    class Meta:
        model= user
        fields = "__all__"
class SuscripciónSerializer(serializers.ModelSerializer):

    class Meta:
        model= suscripción 
        fields = "__all__"