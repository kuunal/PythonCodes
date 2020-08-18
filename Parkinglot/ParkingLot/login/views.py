import jwt
import redis
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from rest_framework import status, generics
from rest_framework.decorators import api_view
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from .serializer import LoginSerializer
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from status_code import get_status_codes
from ParkingLot import settings
from ParkingLot.redis_setup import get_redis_instance 
from .serializer_pass import ResetSerializer
from register.send_mail import send_verification
from register.serializer import RegisterSerializer
from django.utils.http import urlsafe_base64_decode
from ParkingLot.redis_setup import get_redis_instance
from django.utils.encoding import force_text
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

# Create your views here.

class UserLoginViews(APIView):
    serializer_class = LoginSerializer
    redis_instance = get_redis_instance()
    
    def get(self, request):
        return Response({'status':401, 'message':'please login first'})

    @csrf_exempt
    def post(self, request):
        email = request.data['email']
        if email is None:
            return Response(get_status_codes(400))
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(get_status_codes(400))
        if not user.check_password(request.data['password']):
            return Response(get_status_codes(401))
        if  not user.is_active: 
            return Response(get_status_codes(401)) 
        auth_token = jwt.encode({'email':email}, settings.JWT_SECRET_KEY )
        data = {
            "user": email,
            "token": auth_token,
            "status":200
        }
        UserLoginViews.redis_instance.set(email, auth_token)
        return Response(data)


@api_view(('GET',))
def logout(request):
    user_id = get_current_user(request)
    redis_instance = get_redis_instance()
    try:
        redis_instance.delete(user_id)
    except DataError:
        return Response({'status':400, 'message':'Please Login first '})
    return Response({'status':200, 'message':'Logged out successfully '})