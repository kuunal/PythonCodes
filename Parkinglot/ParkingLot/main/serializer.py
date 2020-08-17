from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .get_parking_slot import get_slot
from django.contrib.auth.models import User 
from .models import (ParkingLotModel, ParkingModel, ParkingSlotModel,
                     ParkingTypeModel, VehicleTypeModel)
from ParkingLot.redis_setup import get_redis_instance
from django.core.exceptions import ValidationError
from status_code import get_status_codes
from datetime import datetime
from vehicle.models import VehicleInformationModel as Vehicle
from .services import get_current_user
from vehicle.serializer import VehicleInformationSerializer
from register.models import RoleModel

class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingModel
        fields = '__all__'



class ParkingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingTypeModel
        fields = ('parking_type', 'charge')

class ParkingTypeSerializerForParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingTypeModel
        fields = ('parking_type', 'charge')
        read_only_fields = ('charge',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', )


class ParkingSerializer(serializers.ModelSerializer):
    parking_slot = serializers.CharField(default=get_slot)
    entry_time = serializers.CharField(default=datetime.now())
    parking_type = ParkingTypeSerializerForParkingSerializer(read_only=True)
    vehicle_number =  VehicleInformationSerializer(read_only=True)
    driver_type = UserSerializer(read_only=True)
    class Meta:
        model = ParkingModel    
        fields = ('id','parking_slot','vehicle_number', 'disabled', 'parking_type', 'entry_time', 'exit_time', 'driver_type')
        read_only_fields = ('entry_time', 'parking_slot', 'driver_type')
        depth = 3



    def create(self, validated_data):
        vehicle_number = validated_data.get('vehicle_number')
        parking_model_instance = ParkingModel(**validated_data)
        if len(ParkingSlotModel.objects.filter(vehicle_number=vehicle_number)) > 0:
            raise serializers.ValidationError("vehicle already parked")
        park_vehicle = ParkingSlotModel.objects.filter(vehicle_number=None).first()
        if park_vehicle:
            park_vehicle.slot_id=get_slot()
            park_vehicle.vehicle_number = vehicle_number
        else:
            park_vehicle = ParkingSlotModel.objects.create(slot_id=get_slot(),
                                                    vehicle_number=vehicle_number)
        park_vehicle.save()
        parking_model_instance.save()
        return validated_data

class ParkingSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlotModel
        fields = '__all__'
        depth = 3


class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLotModel
        fields = '__all__'


    def create(self, validated_data):
        lot_object = ""
        if ParkingLotModel.objects.count() > 0:
            lot_object = ParkingLotModel.objects.all()[:1].get()
            lot_object.total_slots = validated_data.get('total_slots')
            lot_object.total_floors = validated_data['total_floors']
        else:
            lot_object = ParkingLotModel(**validated_data)
        lot_object.save()
        return validated_data


