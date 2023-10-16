from rest_framework.router import DefaultRouter
from .views import SuscripciónViewset

router= DefaultRouter()
router.register(r'suscripción',     SuscripciónViewset, basename='suscripción')

urlpatterns = []
urlpatterns += router.urls