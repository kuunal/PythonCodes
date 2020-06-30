from rest_framework import serializers
# from .models import RegisterModel
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

        role = RoleModel(
            role = validated_data['role'],
            charges = charges.get(validated_data['charges'])
        )
        register.save()
        return register


        
role=(
    ('driver','driver'),
    ('police','police'),
    ('security','security'),
    ('owner','owner')
)

class RoleModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role= models.CharField(max_length= 100, choices= role)
    charge= models.IntegerField()
