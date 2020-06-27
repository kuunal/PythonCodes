import jwt
from rest_framework import authentication, exceptions
from rest_framework.authentication import get_authorization_header
from Main import settings
from django.contrib.auth.models import User

def decode(token):
    if not token:
         raise exceptions.AuthenticationFailed("Your token is invalid")
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY)
        user_email=payload.get('email')
        return user_email, payload 
    except jwt.DecodeError as identifier:   
        raise exceptions.AuthenticationFailed("Your token is invalid")
    except jwt.ExpiredSignatureError as indentifier:
        raise exceptions.AuthenticationFailed("your token is expired!")    
    return None
