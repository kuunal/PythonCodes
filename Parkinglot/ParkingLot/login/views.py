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
# from django.contrib import auth
from rest_framework import status
from status_code import get_status_codes
from ParkingLot import settings
from ParkingLot.redis_setup import get_redis_instance 
from .serializer_pass import ResetSerializer
from register.send_mail import send_verification
from register.serializer import RegisterSerializer
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class UserLoginViews(APIView):
    serializer_class = LoginSerializer
    redis_instance = get_redis_instance()
  
    @csrf_exempt
    def post(self, request):
        email = request.data['email']
        if email is None:
            return Response(get_status_codes(400))
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(get_status_codes(401))
        if not user.check_password(request.data['password']):
            return Response(get_status_codes(401))
        if  not user.is_active: 
            return Response(get_status_codes(403)) 
        auth_token = jwt.encode({'email':email}, settings.JWT_SECRET_KEY )
        data = {
            "user": email,
            "token": auth_token,
            "status":200
        }
        UserLoginViews.redis_instance.set(email, auth_token)
        return Response(data)

class ForgotPassView(APIView):
    def get(self, request):
        return render(request, "registration/forgotpassword.html")

    def post(self, request):   
        email = request.data.get('email') 
        host=settings.HOST+"/reset"
        if(len(User.objects.filter(email=email))==0):
            messages.warning(request, "Email doesnt exist")
            return render(request, "registration/forgotpassword.html")            
        send_verification(email, "Reset password link", host) 
        return render(request, "registration/reset.html")

class ResetPassView(APIView):
    def get(self, request, token, email):
        return render(request, "registration/reset.html")
    
    def post(self, request, token, email):
        email = force_text(urlsafe_base64_decode(email))
        password=request.data['password']
            # email = force_text(urlsafe_base64_decode(email))
        user = User.objects.get(email=email)
        serializer = ResetSerializer(user, data=request.data)
        if serializer.is_valid():   
            user.set_password(password)
            user.save()
            return redirect('login')
        messages.warning(request, "Password should contain atleast one Capital, Symbol and number")
        
        
