from django.db import models
from django.contrib.auth.models import User
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


class UserModel(models.Model): 
    email= models.EmailField(max_length= 100)
    role= models.CharField(max_length=100, choices= role)
    password= models.CharField(max_length=100)
