from rest_framework.router import DefaultRouter
from .views import userViewset

router= DefaultRouter()
router.register(r'user', prestamoViewset, basename='user')

urlpatterns = []
urlpatterns += router.urls