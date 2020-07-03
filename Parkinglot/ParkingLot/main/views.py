from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ParkingTypeSerializer, VehicleSerializer, ParkingSerializer
from .get_parking_slot import get_slot
from django.http import HttpResponse
from .models import ParkingTypeModel, VehicleTypeModel, ParkingModel, ParkingSlotModel
from vehicle.models import VehicleInformationModel as vehicle
from ParkingLot.redis_setup import get_redis_instance
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from status_code import get_status_codes
from .services import unpark


class ParkingView(viewsets.ModelViewSet):
    queryset = ParkingModel.objects.all()
    serializer_class = ParkingSerializer
    lookup_field = 'vehicle_number__vehicle_number_plate'


    def perform_create(self, serializer):
        user = get_object_or_404(User,email="asdf@gmail.com")  
        serializer.save(driver_type=user)
     
    def destroy(self, request, *args, **kwargs):
        charges = 0
        try:
            instance = self.get_object()
            charges = unpark(instance)
        except Exception:
            return Response(get_status_codes(404))
        return Response({'message':'Unparked','charges':charges})
        
              

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