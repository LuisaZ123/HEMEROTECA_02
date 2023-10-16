# HEMEROTECA_02
#PARA VALIDAR LOS DATOS QUE SE INGRESAN A LOS MODELOS
Dentro de cada app  en views se agrega:

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def validate_unique(self, data):
        #Para verificar  si el correo electrónico ingresado ya existe en la base de datos
        email = data.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Este correo electrónico ya está en uso"})

        # Para Verificar si el nombre de usuario ya existe en la base de datos
        username = data.get('username')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "Este nombre de usuario ya está en uso"})

        # Si no se encuentran errores de validación, se devuelve None
        return None

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Llama al método validate_unique antes de guardar el objeto
        self.validate_unique(serializer.validated_data)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
