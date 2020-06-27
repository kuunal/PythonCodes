import redis
from rest_framework.decorators import api_view
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from Main import settings
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import get_authorization_header
from Main.redis_setup import get_redis_instance
from . import jwt_decode as jawt
from login import serializer 
import json

class HomeView(APIView):
    redis_instance  = get_redis_instance()

    def get(self, request, email):
        if request.headers.get('x_token'):
            token = request.headers.get('x_token').split(' ')[1]
            user_email, payload = jawt.decode(token)
            for key in HomeView.redis_instance.scan_iter():
                print(key.decode('utf-8') , user_email)
                if key.decode('utf-8') == user_email and token == HomeView.redis_instance.get(user_email).decode('utf-8'):
                    data = User.objects.all().values_list("username", flat=True)
                    user = User.objects.get(email=user_email)
                    data = [ user for user in data ]  
                    data = {'user':str(user), 'data':data, 'status':200}
                    return Response(data) 



        return render(request, "home/home.html") 
            

@api_view(('GET',))
def logout(request):
    token = request.headers.get('x-token').split(' ')[1]
    user_email, payload = jawt.decode(token)
    for key in HomeView.redis_instance:
            if key == user_email and token == HomeView.redis_instance.get(user_email):
                HomeView.redis_instance.delete(key)
                return Response(200)
    return Response(400)
            