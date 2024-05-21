from rest_framework import routers
from .api import UserViewSet,ProductViewSet


router = routers.DefaultRouter()

router.register('api/user',UserViewSet, 'user')
router.register('api/product',ProductViewSet, 'product')

urlpatterns = router.urls
