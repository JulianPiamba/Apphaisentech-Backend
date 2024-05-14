from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ( 'usr_id','usr_name',
                    'usr_last_name','usr_gener',
                    'usr_email','usr_password', 
                    'usr_address','usr_phone',
                    'usr_last_access' )
        read_only_fields = ('usr_id','usr_last_acces')
    