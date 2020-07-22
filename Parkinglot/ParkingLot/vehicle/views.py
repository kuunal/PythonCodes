from django.shortcuts import render
from rest_framework import viewsets
from .models import VehicleInformationModel as Vehicle
from .models import VehicleTypeModel 
from .serializer import VehicleInformationSerializer
from rest_framework.response import Response
from status_code import get_status_codes
from main.views import LoginRequiredMixin
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError

class VehicleView(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleInformationSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('color','brand','vehicle_number_plate','vehicle_owner_email','vehicle_type__vehicle_type')
   
    def create(self, request):
        vehicle_type = request.data.get('vehicle_type')
        vehicle_type_object = VehicleTypeModel.objects.get(vehicle_type = vehicle_type)
        serializer = VehicleInformationSerializer(data = request.data)
        if serializer.is_valid():   
            if len(Vehicle.objects.filter(vehicle_number_plate=request.data['vehicle_number_plate']))>0:
                return Response({'status':400,'message':'Vehicle Already exist'})
            serializer.save(vehicle_type = vehicle_type_object)
            return Response(serializer.data)
        return Response(serializer.errors)