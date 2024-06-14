from rest_framework import serializers
from .models import User,Product,Role,Sale,PaymentMethod,PaymentHistory,ShoppingCartItem,ShoppingCart

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = [ 'user','username','password']
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (  'product','pro_name','pro_price','pro_description'
                  ,'pro_stock','pro_category')
       
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id','rol_name','rol_description')

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id','user','product','')
    
    
class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ('id', 'pym_method', 'pym_icon')

class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = ('id', 'pyh_amount', 'pym_date', 'user', 'pym_method')

class ShoppingCartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = ShoppingCartItem
        fields = ('id', 'cart', 'product', 'shoi_quantity')

class ShoppingCartSerializer(serializers.ModelSerializer):
    items = ShoppingCartItemSerializer(many=True, read_only=True, source='shoppingcartitem_set')

    class Meta:
        model = ShoppingCart
        fields = ('id', 'user','items')