from rest_framework import serializers
# from .models import RegisterModel
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

user_model = get_user_model() 

class RegisterSerializer(serializers.ModelSerializer):



    class Meta:
        model = User
        fields = ['username','email','password','is_active'] 


    def create(self, validated_data):

        register = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        register.is_active=False
        register.set_password(validated_data['password'])
        register.save()
        return register