from rest_framework.router import DefaultRouter
from .views import prestamoViewset

router= DefaultRouter()
router.register(r'prestamo', prestamoViewset, basename='id_prestamo')

urlpatterns = []
urlpatterns += router.urls