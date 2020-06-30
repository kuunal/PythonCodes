from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializer import RegisterSerializer
from django.http import JsonResponse
# from .models import RegisterModel
from rest_framework.response import Response
from rest_framework import status
from Main import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from Tools.scripts import generate_token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .send_mail import send_verification
from status_code import get_status_codes
from Main.redis_setup import get_redis_instance
from .serializer import RegisterSerializer

class RegisterViews(APIView):

    def get(self, request):
        return render(request, 'register/register.html')

    def post(self, request):
        user_email = request.POST['email']
        queryset = User.objects.all()
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            send_verification(user_email)
            return Response(get_status_codes(200))
        return Response(get_status_codes(400)) 
    
    
def verify_user(request, token, email):
    id = force_text(urlsafe_base64_decode(token))
    user = User.objects.get(email=id)
    user.is_active = True
    user.save()
    return redirect('login')

@api_view(('GET',))
def check_login(request):
    redis_instance = get_redis_instance()
    email = request.headers.get('x_token')
    if redis_instance.get(email):
        return Response(202)
    return Response(300)
