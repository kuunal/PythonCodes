from rest_framework import serializers
from staff.models import UserModel 
from .models import ParkingModel, VehicleTypeModel, ParkingTypeModel, ParkingLotModel, ParkingSlotModel
from get_parking_slot import get_slots

# class ParkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ParkingModel
#         fields = '__all__'

# class VehicleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VehicleTypeModel
#         fields = '__all__'

# class ParkingTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ParkingTypeModel
#         fields = '__all__'


# class ParkingSerializer(serializers.ModelSerializer):
#     # parking_type = serializers.RelatedField(source = 'parkingtypeserializer.parking_type', read_only= True)
#     # vehicle_type = serializers.RelatedField(source = 'vehicletypeserializer.vehicle_type', read_only= True)

#     # parking_type = serializers.SerializerMethodField('get_parking_type')
#     # # # parking_type = serializers.IntegerField(write_only=True)
#     # # vehicle_type = serializers.SerializerMethodField('get_vehicle_type')

#     # # parking_type = serializers.RelatedField(source='parkingtypemode', read_only=True)
#     # vehicle_type = serializers.RelatedField(source='vehicle_type', read_only=True)
     
#     parking_type = ParkingTypeSerializer(many=False, read_only=True)
#     vehicle_type = VehicleSerializer(many=False, read_only=True)
    
#     class Meta:
#         model = ParkingModel    
#         fields = ['vehicle_number', 'disabled', 'parking_type', 'vehicle_type']

    # def get_parking_type(self, obj):
    #     return ParkingTypeSerializer.objects.get(parking_type=obj.parking_type)

    # def get_vehicle_type(self, obj):
    #     return VehicleSerializer.objects.get(vehicle_type=obj.vehicle_type)

    # def create(self, validated_data):
    #     parking_type = validated_data['parking_type']
    #     vehicle_type = validated_data['vehicle_type']
    #     self.driver_type = VehicleTypeModel.objects.get(vehicle_type=vehicle_type)
    #     self.parking_type = ParkingTypeModel.objects.get(parking_type=parking_type)
    #     self.save()
    #     return self
        # ParkingSlotModel.objects.create(driver=None, parking_type=)


# class ParkingLotSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ParkingLotModel
#         fields = '__all__'






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
    # parking_type = serializers.RelatedField(source = 'parkingtypeserializer.parking_type', read_only= True)
    # vehicle_type = serializers.RelatedField(source = 'vehicletypeserializer.vehicle_type', read_only= True)

    # parking_type = ParkingTypeSerializer( read_only = True)
    # # parking_type = serializers.IntegerField(write_only=True)
    # vehicle_type = VehicleSerializer(read_only = True)

    class Meta:
        model = ParkingModel    
        fields = ('parking_slot','vehicle_number', 'disabled', 'parking_type', 'vehicle_type')

    def create(self, validated_data):
        ParkingSlotModel.objects.create()


  
     
class ParkingLotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParkingLotModel
        fields = '__all__'

