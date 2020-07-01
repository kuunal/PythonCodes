from django.db import models 
from django.contrib.auth.models import User, AbstractBaseUser
from django.core.validators import RegexValidator


role=(
    ('driver','driver'),
    ('police','police'),
    ('security','security'),
    ('owner','owner')
)
class RoleModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length= 100, choices= role)
    charge= models.IntegerField()



class RegisterUser(AbstractBaseUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^[0-9]{10}$', message="Phone number must be entered")
    role= models.ForeignKey(RoleModel, on_delete=models.DO_NOTHING, related_name="user_roles")
    is_active = models.BooleanField(default=False)
    staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
