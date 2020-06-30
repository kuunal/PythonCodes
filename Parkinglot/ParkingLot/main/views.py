from django.shortcuts import render
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ParkingTypeSerializer, VehicleSerializer, ParkingSerializer
from .get_parking_slot import get_slots
from django.http import HttpResponse
from .models import ParkingTypeModel, VehicleTypeModel, ParkingModel


class ParkingView(viewsets.ModelViewSet):
    queryset = ParkingModel.objects.all()
    serializer_class = ParkingSerializer

class VehicleTypeView(viewsets.ModelViewSet):
    queryset = VehicleTypeModel.objects.all()
    serializer_class = VehicleTypeModel

class ParkingTypeView(viewsets.ModelViewSet):
    queryset = ParkingTypeModel.objects.all()
    serializer_class = ParkingTypeModel








'''
vehicle number, token no, in time,  driver type, parking, 
while taking out unpark: Slot number, vehicle number,out time, as per the time calc hrs

id, Parking slot(1 - 400), Vehicle number, Vehicle type(foreign from parking type), Entry 
time, Parking type(foreign key from parking type), driver type( Foreign key from User ),
Disabled(True/False), exit time

'''