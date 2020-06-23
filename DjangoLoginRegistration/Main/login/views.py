from rest_framework import status, generics
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

from django.contrib.auth.views import LoginView
from .serializer import LoginSerializer
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from register.models import RegisterModel
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import auth
from rest_framework import status

# Create your views here.

class LoginViews(APIView):
    serializer_class = LoginSerializer
    def get(self, request):
        return render(request,'registration/login.html')

    def post(self, request):
        email = request.data['email']
        if email is None:
            return Response(status=400)
            
        user = User.objects.get(email=email)
        if not user.check_password(request.data['password']):
            return HttpResponse('failed')
        return HttpResponse( 'success')