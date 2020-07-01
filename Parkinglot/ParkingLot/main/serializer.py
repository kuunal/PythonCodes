from rest_framework import serializers
from .models import ParkingModel, VehicleTypeModel, ParkingTypeModel, ParkingLotModel, ParkingSlotModel
from .get_parking_slot import get_slots


class ParkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParkingModel
        fields = '__all__'

class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleTypeModel
        fields = '__all__'

class ParkingTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParkingTypeModel
        fields = '__all__'


class ParkingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ParkingModel    
        fields = ('parking_slot','vehicle_number', 'disabled', 'parking_type', 'vehicle_type')

    def create(self, validated_data):
        ParkingSlotModel.objects.create()


  
     
class ParkingLotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParkingLotModel
        fields = '__all__'

