
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes,authentication_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import User, Product, ShoppingCart, ShoppingCartItem
from .serializers import UserSerializer, ProductSerializer, ShoppingCartSerializer, ShoppingCartItemSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ShoppingCartSerializer
    
    @action(detail=False, methods=['post'],url_path='add')
    def add_to_cart(self, request):
        print("entro en añadir producto")
        user = request.user
        print(request.user)
        if not request.user.is_authenticated:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_403_FORBIDDEN)
        product = request.data.get('product')
        shoI_quantity = request.data.get('shoI_quantity', 1)
        print(product)

        try:
            product = Product.objects.get(product=product)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        print(request.user),
        print(type(request.user)),
        print(product)
        cart, created = ShoppingCart.objects.get_or_create(user=user)
        cart_item, created = ShoppingCartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            cart_item.shoI_quantity += shoI_quantity
        else:
            cart_item.shoI_quantity = shoI_quantity
        cart_item.save()

        return Response({'message': 'Product added to cart'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def remove_from_cart(self, request):
        user = request.data.get('user')
        product = request.data.get('product')

        try:
            product = Product.objects.get(id=product)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        cart = ShoppingCart.objects.get(user=user)
        try:
            cart_item = ShoppingCartItem.objects.get(cart=cart, product=product)
            cart_item.delete()
            return Response({'message': 'Product removed from cart'}, status=status.HTTP_200_OK)
        except ShoppingCartItem.DoesNotExist:
            return Response({'error': 'Product not in cart'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'],url_path='view')
    def view_cart(self, request):
        user = request.user
        try:
            cart = ShoppingCart.objects.get(user=user)
        except ShoppingCart.DoesNotExist:
            return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

        cart_items = ShoppingCartItem.objects.filter(cart=cart)
        cart_data = ShoppingCartSerializer(cart).data
        cart_data['items'] = ShoppingCartItemSerializer(cart_items, many=True).data

        return Response(cart_data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def update_quantity(self, request):
        user = request.user
        product = request.data.get('product')
        quantity = request.data.get('quantity')

        try:
            product = Product.objects.get(id=product)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        cart = ShoppingCart.objects.get(user=user)
        try:
            cart_item = ShoppingCartItem.objects.get(cart=cart, product=product)
            cart_item.quantity = quantity
            cart_item.save()
            return Response({'message': 'Quantity updated'}, status=status.HTTP_200_OK)
        except ShoppingCartItem.DoesNotExist:
            return Response({'error': 'Product not in cart'}, status=status.HTTP_404_NOT_FOUND)