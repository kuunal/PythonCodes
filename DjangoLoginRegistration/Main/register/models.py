from django.db import models 
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from Main import settings

# Create your models here.
class RegisterModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    # def create(self, validate_data):
    #     user = User(
    #         first_name = validate_data['first_name'],
    #         last_name = validate_data['last_name'],
    #         email = validate_data['email'],
    #     )
    #     user.set_password(validate_data['password'])
    #     user.save()
    #     return user

     