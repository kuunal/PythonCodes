import re
from django.db import models 
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
# User = get_user_model()

role=(
    ('driver','driver'),
    ('police','police'),
    ('security','security'),
    ('owner','owner')
)
class RoleModel(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length= 100, choices= role)
    charge= models.IntegerField()




