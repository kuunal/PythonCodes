import re
from django.db import models 
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

role=(
    ('driver','driver'),
    ('security','security'),
    ('owner','owner')
)
class RoleModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length= 100, choices= role)
    charge= models.IntegerField()

    def __str__(self):
        return f'{self.user.username} is {self.role}'
