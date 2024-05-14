from rest_framework import routers
from .api import UserViewSet


router = routers.DefaultRouter()

router.register('api/core',UserViewSet, 'core')

urlpatterns = router.urls
