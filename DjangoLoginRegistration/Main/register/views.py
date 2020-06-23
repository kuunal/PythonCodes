from django.shortcuts import redirect, render
from rest_framework.views import APIView
from .serializer import RegisterSerializer
from django.http import JsonResponse
from .models import RegisterModel
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

class RegisterViews(APIView):

    def get(self, request):
        return render(request, 'register/register.html')

    def post(self, request):
        user_email = request.POST['email']
        print(request.data)
        queryset = RegisterModel.objects.all()
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            send_verification(user_email)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
    
    
def verify_user(request, token, email):
    id = force_text(urlsafe_base64_decode(email))
    user = User.objects.get(email=id)
    user.is_active = True
    user.save()
    return redirect('login')
