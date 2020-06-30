import re
from .models import UserModel
from django.core.exceptions import ValidationError
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=25)
    class Meta:
        model = UserModel
        fields='__all__'
    


    def validate(self, data):
        password = data['password']
        password1 = data['password1']
        if password != password1:
            raise ValidationError("Confirm passowrd doest match")
        if re.match("^(?=.*[0-9])(?=.*[A-Z])(?=[a-zA-Z0-9]*[^a-zA-Z0-9][a-zA-Z0-9]*$).{8,}",password):
            return data
        raise ValidationError("Passowrd doont match format")

    
