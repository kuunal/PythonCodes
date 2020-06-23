from django.db import models 
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser
from Main import settings


# class RegisterManager(BaseUserManager): 
#     def create_user(self, email, username, password=None):
#         us

class RegisterModel(AbstractBaseUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['username','email']
    USERNAME_FIELD = 'email'



    # def __str__(self):
    #     return self.first_name

    # def create(self, validate_data):
    #     user = User(
    #         first_name = validate_data['first_name'],
    #         last_name = validate_data['last_name'],
    #         email = validate_data['email'],
    #     )
    #     user.set_password(validate_data['password'])
    #     user.save()
    #     return user

     