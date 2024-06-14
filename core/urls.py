
from django.contrib import admin
from django.urls import path, include , re_path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .api import UserViewSet, ProductViewSet, ShoppingCartViewSet
from . import views

router = routers.DefaultRouter()
router.register('api/user', UserViewSet, 'user')
router.register('api/product', ProductViewSet, 'product')
router.register('api/cart', ShoppingCartViewSet, 'cart')

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth/login/', obtain_auth_token, name='login'),  # Aquí se obtiene el token
    re_path('login', views.login),
    re_path('register', views.register),
    re_path('profile', views.profile)
]
