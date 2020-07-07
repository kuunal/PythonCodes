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
from django.views.generic.list import ListView 
from status_code import get_status_codes
from .services import unpark
from .tasks import send_mail_to_user_when_vehicle_is_parked
from .authenticate import Autheticate 
from rest_framework import generics
from rest_framework.decorators import action

class ParkingView(viewsets.ModelViewSet):
    queryset = ParkingModel.objects.all()
    serializer_class = ParkingSerializer
    permission_classes = (Autheticate,)
    # lookup_field = 'vehicle_number__vehicle_number_plate'

    @action(detail=False, methods=["GET"])
    def parked(self, request, *args, **kwargs):
        queryset = ParkingModel.objects.filter(exit_time=None)
        serializer = ParkingSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=["GET"])
    def records(self, request, pk=None):
        print(pk)
        queryset = ParkingModel.objects.filter(vehicle_number__vehicle_number_plate=pk)
        print(queryset)
        serializer = ParkingSerializer(queryset, many=True)
        return Response(serializer.data)
    

    def perform_create(self, serializer):
        user = get_object_or_404(User,email="zzzaxwk@gmail.com")  
        serializer.save(driver_type=user)
        vehicle_object = vehicle.objects.get(id=serializer.data['vehicle_number'])
        send_mail_to_user_when_vehicle_is_parked.delay(vehicle_object.vehicle_owner_email)
     
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





