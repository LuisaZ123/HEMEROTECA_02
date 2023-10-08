from rest_framework.router import DefaultRouter
from .views import libroViewset

router= DefaultRouter()
router.register(r'libros', libroViewset, basename='user')

urlpatterns = []
urlpatterns += router.urls