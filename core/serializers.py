from rest_framework import serializers
from .models import User,Product,Role,Sale

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ( 'user','usr_name',
                    'usr_last_name','usr_gener',
                    'usr_email','usr_password', 
                    'usr_address','usr_phone',
                    'usr_last_access' )
        read_only_fields = ('user','usr_last_acces')
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (  'product','pro_name','pro_price','pro_description',
                    'pro_review','pro_stock','pro_image','pro_category')
        read_only_fields = ('pro_id',)
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id','rol_name','rol_description')

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id','user','product','')
    
    
    