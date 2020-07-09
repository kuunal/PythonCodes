from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleInformationModel as Vehicle
from .serializer import VehicleInformationSerializer
from rest_framework.response import Response
from status_code import get_status_codes
from main.views import LoginRequiredMixin
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

class VehicleView(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleInformationSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('color','brand','vehicle_number_plate','vehicle_owner_email','vehicle_type__vehicle_type')
   
   