from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializer import RegisterSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ParkingLot import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from status_code import get_status_codes
from ParkingLot.redis_setup import get_redis_instance
from .serializer import RegisterSerializer, RoleSerializer
from main.tasks import send_verification_to_user
from .models import RoleModel
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from main.views import LoginRequiredMixin, DriverPermissions

class RegisterViews(APIView):

    serializer_class = RegisterSerializer
    def post(self, request):
        queryset = User.objects.all()
        user_email = request.data['email']
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            send_verification_to_user.delay(user_email)
            return Response(get_status_codes(201))
        return Response(serializer.errors)
    
@api_view(('GET',))
def verify_user(request, token):
    email = force_text(urlsafe_base64_decode(token))
    user = User.objects.get(email=email)
    if user.is_active == True:
        return Response(get_status_codes(400))
    user.is_active = True
    user.save()
    return redirect('login')


class RegisterListView(LoginRequiredMixin, ListAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = '__all__'
    permission_classes = (DriverPermissions,)
    
    