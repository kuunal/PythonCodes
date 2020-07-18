from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ParkingTypeSerializer, ParkingSerializer, ParkingLotSerializer#, ParkingFilter
from .get_parking_slot import get_slot
from django.http import HttpResponse
from .models import ParkingTypeModel, VehicleTypeModel, ParkingModel, ParkingSlotModel, ParkingLotModel
from register.models import RoleModel
from vehicle.models import VehicleInformationModel as vehicle
from ParkingLot.redis_setup import get_redis_instance
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.views.generic.list import ListView 
from status_code import get_status_codes
from .services import unpark, get_current_user
from .tasks import send_mail_to_user_when_vehicle_is_parked
from rest_framework.permissions import BasePermission
from rest_framework import generics
from rest_framework.decorators import action
from vehicle.serializer import VehicleSerializer
from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from main.serializer import ParkingSlotSerializer


class LoginRequiredMixin():
    def dispatch(self, request, *args, **kwargs):
        if get_current_user(request):
            return super().dispatch(request, *args, **kwargs)
        return redirect('login')

class LotSizeRequiredMixin():
    def dispatch(self, request, *args, **kwargs):
        if ParkingLotModel.objects.count() > 0:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/lot')

class DriverPermissions(BasePermission):
    def has_permission(self, request, view):
        try:
            role = RoleModel.objects.get(user__email = get_current_user(request)).role
        except RoleModel.DoesNotExist:
            return Response(get_status_codes(401))
        else:
            if role.lower() == "driver" : 
                if request.method == "POST" or request.method == "DELETE":
                    return True
                return False
            return True

class ParkingView(LoginRequiredMixin, LotSizeRequiredMixin, viewsets.ModelViewSet):
    queryset = ParkingModel.objects.all()
    serializer_class = ParkingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'
    permission_classes = (DriverPermissions,)

    @action(detail=True, methods=["GET"])
    def records(self, request, pk=None):
        queryset = ParkingModel.objects.filter(vehicle_number__vehicle_number_plate=pk)
        serializer = ParkingSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"])
    def parked(self, request, *args, **kwargs):        
        queryset = ParkingModel.objects.filter(exit_time=None)
        serializer = ParkingSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        user_email = get_current_user(request)
        try:
            user = User.objects.get(email=user_email)
        except User.DoesNotExist:
            return Response({'status':400,'message':'Admin is not available'})
        vehicle_number = request.data.get('vehicle_number')
        parking_type = request.data.get('parking_type')
        vehicle_object = vehicle.objects.get(vehicle_number_plate = vehicle_number)
        parking_type_object = ParkingTypeModel.objects.get(parking_type = parking_type)
        serialzier = ParkingSerializer(data = request.data)
        if serialzier.is_valid():
            serialzier.save(driver_type=user, vehicle_number = vehicle_object, parking_type = parking_type_object)
            send_mail_to_user_when_vehicle_is_parked.delay(vehicle_object.vehicle_owner_email)
            return Response(serialzier.data)
        return Response(get_status_codes(400))


    def destroy(self, request, *args, **kwargs):
        charges = 0
        try:
            instance = self.get_object()
            charges = unpark(instance)
        except Exception:
            return Response({'status':400,'message':'No such vehicle parked'})
        return Response({'message':'Unparked','charges':charges})



class VehicleTypeView(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = VehicleTypeModel.objects.all()
    serializer_class = VehicleSerializer

class ParkingTypeView(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = ParkingTypeModel.objects.all()
    serializer_class = ParkingTypeSerializer

class ParkingLotView(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = ParkingLotModel.objects.all()
    serializer_class = ParkingLotSerializer

