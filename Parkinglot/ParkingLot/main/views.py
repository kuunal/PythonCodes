from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ParkingTypeSerializer, VehicleSerializer, ParkingSerializer, ParkingLotSerializer#, ParkingFilter
from .get_parking_slot import get_slot
from django.http import HttpResponse
from .models import ParkingTypeModel, VehicleTypeModel, ParkingModel, ParkingSlotModel, ParkingLotModel
from vehicle.models import VehicleInformationModel as vehicle
from ParkingLot.redis_setup import get_redis_instance
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.views.generic.list import ListView 
from status_code import get_status_codes
from .services import unpark, get_current_user
from .tasks import send_mail_to_user_when_vehicle_is_parked
# from .authenticate import Autheticate 
from rest_framework import generics
from rest_framework.decorators import action
from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend

class LoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        redis_instance = get_redis_instance()
        for key in redis_instance.scan_iter():
            if key:
                return super().dispatch(request, *args, **kwargs)
        return redirect('login')

class LotSizeRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if ParkingLotModel.objects.count() > 0:
            return super().dispatch(request, *args, **kwargs)
        return redirect('lot')


class ParkingView(LoginRequiredMixin, LotSizeRequiredMixin, viewsets.ModelViewSet):
    queryset = ParkingModel.objects.all()
    serializer_class = ParkingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = '__all__'

    # @action(detail=False, methods=["GET"])
    # def parked(self, request, *args, **kwargs):
    #     queryset = ParkingModel.objects.filter(exit_time=None)
    #     serializer = ParkingSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    # @action(detail=True, methods=["GET"])
    # def records(self, request, pk=None):
    #     queryset = ParkingModel.objects.filter(vehicle_number__vehicle_number_plate=pk)
    #     serializer = ParkingSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    # @action(detail=True, methods=["GET"])
    # def color(self, request, pk=None):
    #     queryset = ParkingModel.objects.filter(vehicle_number__color=pk)
    #     serializer = ParkingSerializer(queryset, many=True)
    #     return Response(serializer.data)
    

    def perform_create(self, serializer):
        user_email = get_current_user().decode("utf-8")
        user = get_object_or_404(User,email=user_email)  
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

  

class VehicleTypeView(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = VehicleTypeModel.objects.all()
    serializer_class = VehicleSerializer

class ParkingTypeView(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = ParkingTypeModel.objects.all()
    serializer_class = ParkingTypeSerializer

class ParkingLotView(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = ParkingLotModel.objects.all()
    serializer_class = ParkingLotSerializer

# class ParkingSearchView(LoginRequiredMixin, APIView):
#     serializer_class = ParkingFilter
#     def post(self, request):
#         info = ParkingSlotModel.objects.all()
#         info_filter = 
    