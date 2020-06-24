from django import forms
# from register.models import RegisterModel
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginSerializer(serializers.ModelSerializer):
    class Meta:    
        model = User
        fields = ['email','password']
    
    def validate(self, data):
        email=data.get('email')
        user =  User.objects.filter(email=email)
        if user.exists() and user.get('is_active') == True :
            if user.check_password(data['password']):
                return data
        else:
            raise ValidationError("Invalid")    
       
       