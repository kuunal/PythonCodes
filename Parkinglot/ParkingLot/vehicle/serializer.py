from rest_framework import serializers
from .models import VehicleInformationModel
from django.core.exceptions import ValidationError


class VehicleInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model =  VehicleInformationModel
        fields = '__all__'

    def validate_color(self, value):
        if any(char.isdigit() for char in value): 
            raise ValidationError("Please provide proper color!")
        return value

    def create(self, validated_data):
        if len(VehicleInformationModel.objects.filter(vehicle_number_plate=validated_data['vehicle_number_plate']))>0:
            raise ValidationError("Vehicle already in database")
        
        vehicle =  VehicleInformationModel(**validated_data)
        vehicle.save()
        return vehicle