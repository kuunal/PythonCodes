from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleInformationModel as Vehicle
from .serializer import VehicleInformationSerializer
from rest_framework.response import Response
from status_code import get_status_codes


class VehicleView(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleInformationSerializer
