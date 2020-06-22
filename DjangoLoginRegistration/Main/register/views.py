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
from .token import generate_token


class RegisterViews(APIView):

    def get(self, request):
        return render(request, 'register/register.html')

    def post(self, request):
        to = request.POST['email']
        queryset = RegisterModel.objects.all()
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            self.send_verification(to)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
    
    def send_verification(self, user_email):
        user = RegisterModel.objects.filter(email=user_email)
        subject = "Account created successfully"
        message = "Thank you! Your account has been created. Please click on the link below to start things up."
        # html_message = '<a href="http://localhost:8000/verify-user/' + user_email +'">click here </a>' 
        html_message = render_to_string('register/activate.html',{
            'user_name' : user.values_list('first_name', flat=True),
            'uid' : urlsafe_base64_encode(force_bytes(user.values_list('id', flat=True)[0])),
            'email': urlsafe_base64_encode(force_bytes(user_email))
        })
        from_email = settings.EMAIL_HOST_USER
        to_list = [user_email,]
        send_mail(subject, message, from_email, to_list, html_message=html_message )

def verify_user(request, token, email):
    id = force_text(urlsafe_base64_decode(token))
    user = RegisterModel.objects.filter(id=id)
    print(user)
    user.is_verified = True
    return redirect('login')
