from rest_framework.router import DefaultRouter
from .views import userViewset, SuscriciónViewset, CreateUserView

router= DefaultRouter()
router.register(r'user', userViewset, basename='user')
router.register(r'suscripción', SuscriciónViewset, basename='Suscripción')

urlpatterns = [
     path('api/sign-up/', TokenObtainPairView.as_view(), name='create_user'),
]
urlpatterns += router.urls