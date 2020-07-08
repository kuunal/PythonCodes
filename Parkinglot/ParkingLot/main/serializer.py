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

class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingModel
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleTypeModel
        fields = ['vehicle_type', 'charge']

class ParkingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingTypeModel
        fields = ('parking_type', 'charge')


class ParkingSerializer(serializers.ModelSerializer):
    parking_slot = serializers.HiddenField(default=get_slot)
    entry_time = serializers.HiddenField(default=datetime.now())
    class Meta:
        model = ParkingModel    
        fields = ('parking_slot','vehicle_number', 'disabled', 'parking_type', 'vehicle_type', 'entry_time')

    def create(self, validated_data):
        user = get_object_or_404(User,email=get_current_user().decode("utf-8")) 
        vehicle_number = validated_data.get('vehicle_number').vehicle_number_plate

        parking_model_instance = ParkingModel(**validated_data)
        if len(ParkingSlotModel.objects.filter(vehicle_number=vehicle_number)) > 0:
            raise ValidationError("vehicle already parked")
            return
        park_vehicle = ParkingSlotModel.objects.filter(vehicle_number="null").first()
        if park_vehicle:
            slot_id=get_slot()
            park_vehicle.vehicle_number = vehicle_number
            park_vehicle.driver = user
            parking_type=validated_data.get('parking_type')
        else:
            park_vehicle = ParkingSlotModel.objects.create(slot_id=get_slot(),
                                                    driver=user,
                                                    parking_type=validated_data.get('parking_type'),
                                                    vehicle_number=vehicle_number)
        park_vehicle.save()
        parking_model_instance.save()
        return validated_data

class ParkingSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlotModel
        fields = '__all__'


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
