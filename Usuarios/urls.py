from rest_framework.router import DefaultRouter
from .views import userViewset, SuscriciónViewset

router= DefaultRouter()
router.register(r'user', userViewset, basename='user')
router.register(r'suscripción', SuscriciónViewset, basename='user')

urlpatterns = []
urlpatterns += router.urls