import re
from rest_framework import serializers
from .models import RoleModel
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


charges={
    'owner': 0,
    'security': 3,
    'driver': 10
}
role=(
    ('driver','driver'),
    ('security','security'),
    ('owner','owner')
)

class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=role)
    class Meta:
        model = User
        fields = ('username','email','password','role') 

    def validate(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        if not re.match("^(?=.*[0-9])(?=.*[A-Z])(?=[a-zA-Z0-9]*[^a-zA-Z0-9][a-zA-Z0-9]*$).{8,}", password):
            raise serializers.ValidationError("Please include atleast one capital, number and symbol ")
        input_email = validated_data['email']
        if len(User.objects.filter(email=input_email)) > 0 :
            raise serializers.ValidationError("Email already exists")
        return validated_data
        
    def create(self, validated_data):
        
        registered_user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        registered_user.is_active=False
        registered_user.set_password(validated_data['password'])
        registered_user.save()
        role = validated_data['role']
        user_role = RoleModel(user=registered_user,role=role, charge=charges[role])
        user_role.save()
        return registered_user





class RoleSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()
    class Meta:
        model = RoleModel
        fields = ('role', 'user') 

    

        
