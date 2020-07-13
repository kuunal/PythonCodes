from rest_framework import serializers
from .models import VehicleInformationModel
from django.core.exceptions import ValidationError
from .models import VehicleTypeModel

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleTypeModel
        fields = ['vehicle_type', 'charge']
        

class VehicleSerializer1(serializers.ModelSerializer):
    class Meta:
        model = VehicleTypeModel
        fields = ['vehicle_type', 'charge']
        read_only_fields = ('charge',)


class VehicleInformationSerializer(serializers.ModelSerializer):
    vehicle_type = VehicleSerializer1(read_only=True)
    class Meta:
        model =  VehicleInformationModel
        fields = ['color','vehicle_number_plate' ,'brand','vehicle_owner', 'vehicle_owner_email', 'vehicle_type'] #'__all__'
     

    def validate_color(self, value):
        if any(char.isdigit() for char in value): 
            raise ValidationError("Please provide proper color!")
        return value

