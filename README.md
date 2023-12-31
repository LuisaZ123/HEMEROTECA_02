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
#PARA CREAR EL ESTADO ACTIVO A UN PRESTAMO Y VERIFICARLO AL GENERAR OTRO PRESTAMO 

1. Crear una nueva función llamada get_absolute_url para el modelo Prestamo en el archivo de views.
def get_absolute_url(self):
        return Response('prestamo-detail', kwargs={'pk': self.pk})
2. Crear una nueva función llamada is_late para el modelo Prestamo en views
def is_late(self):
        if self.fecha_de_devolución is None:
            return False
        return self.fecha_de_devolución > self.fecha_de_vencimiento
3. Crear una nueva función llamada get_debt_collection_metric para el modelo Prestamo.
def get_debt_collection_metric(prestamos):
    total_amount_owed = 0
    for prestamo in prestamos:
        if prestamo.is_late():
            total_amount_owed += prestamo.amount_owed
    return total_amount_owed
#PARA CREAR EL SISTEMA DE AUTENTICACIÓN#
Para establecer los permisos por tipo de usurario se agrega cada uno de las clasificaciones en models de la app de usuarios 
class user(AbstractUser):
    ROLES_HEMEROTECA: (
        1, "BIBLIOTECARIO",
        2,"ARCHIVISTA",
        3, "INVESTIGADOR",
        4, "ESTUDIANTE", 
        5, "LECTOR",
        6, "ADMINISTRADOR"
    )
y se establece el permiso en el archivo de views de las demás apps:
class CreatePermision(BasePermission):
    def has_permission(self, request, view):
        print(f"Pase por el permiso {request.user.id}")
        if view.action == "create" : return request.user.rol == #Número de clasificación de usuario
        return True
#DOCUMENTACIÓN CON SWAGGER#
1. Instalar la libreria correcta pip install -U drf-yasg
2. Para la validación instalar pip install -U drf-yasg[validation]
3. En el archivo settings.py del proyecto general agregar 'drf_yasg' en INSTALLED APPS
4. Se agrega al archivo de urls.py del proyecto general:
   from django.urls import re_path
   from rest_framework import permissions
   from drf_yasg.views import get_schema_view
   from drf_yasg import openapi
5. Agregar al archivo de urls.py y cambiar los datos:
   
   schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

7. En el mismo archivo se copia:
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ...
]
8. Comprobar con python .\manage.py runserver

