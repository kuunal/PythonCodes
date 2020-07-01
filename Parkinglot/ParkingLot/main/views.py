from django.shortcuts import render
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ParkingTypeSerializer, VehicleSerializer, ParkingSerializer
from .get_parking_slot import get_slot
from django.http import HttpResponse
from .models import ParkingTypeModel, VehicleTypeModel, ParkingModel, ParkingSlotModel
from ParkingLot.redis_setup import get_redis_instance
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class ParkingView(viewsets.ModelViewSet):
    queryset = ParkingModel.objects.all()
    serializer_class = ParkingSerializer
    
    # def perform_create(self, serializer):
       
        
        

class VehicleTypeView(viewsets.ModelViewSet):
    queryset = VehicleTypeModel.objects.all()
    serializer_class = VehicleSerializer

class ParkingTypeView(viewsets.ModelViewSet):
    queryset = ParkingTypeModel.objects.all()
    serializer_class = ParkingTypeSerializer




'''
vehicle number, token no, in time,  driver type, parking, 
while taking out unpark: Slot number, vehicle number,out time, as per the time calc hrs

id, Parking slot(1 - 400), Vehicle number, Vehicle type(foreign from parking type), Entry 
time, Parking type(foreign key from parking type), driver type( Foreign key from User ),
Disabled(True/False), exit time

'''