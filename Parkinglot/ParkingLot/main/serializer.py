from rest_framework import serializers
from .get_parking_slot import get_slot
from django.contrib.auth.models import User 
from .models import (ParkingLotModel, ParkingModel, ParkingSlotModel,
                     ParkingTypeModel, VehicleTypeModel)
from ParkingLot.redis_setup import get_redis_instance
from django.core.exceptions import ValidationError


class ParkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParkingModel
        fields = '__all__'

class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleTypeModel
        fields = ['vehicle_type', 'charge', 'url']

class ParkingTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParkingTypeModel
        fields = ('parking_type','url', 'charge')


class ParkingSerializer(serializers.HyperlinkedModelSerializer):
    parking_slot = serializers.HiddenField(default=get_slot())
    class Meta:
        model = ParkingModel    
        fields = ('parking_slot','vehicle_number', 'disabled', 'parking_type', 'vehicle_type', 'exit_time')

    def create(self, validated_data):
        # user = is_authentic(request.headers.get('x_token'))
        user = User.objects.get(email="zzzaxwk@gmail.com") #testing
        if not user:
            raise ValidationError("Unauthorized")
        park_vehicle = ParkingSlotModel( slot_id = get_slot(),
                                            driver = user,
                                            parking_type = validated_data.get('parking_type') )
        park_vehicle.save()
        

class ParkingLotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParkingLotModel
        fields = '__all__'
