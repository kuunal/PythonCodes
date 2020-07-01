from rest_framework import serializers
from .models import RoleModel
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



user_model = get_user_model() 

charges={
    'owner': 0,
    'police': 2,
    'security': 3,
    'driver': 10
}
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = ('role',) 

class RegisterSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    class Meta:
        model = User
        fields = ('username','email','password','role') 

    def create(self, validated_data):

        registered_user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        registered_user.is_active=False
        registered_user.set_password(validated_data['password'])

        registered_user.save()
        return registered_user


        
