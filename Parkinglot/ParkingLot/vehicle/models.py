from django.db import models
# Create your models here.

vehicle_type= (
    ('car','car'),
    ('bike','bike')
)
class VehicleTypeModel(models.Model):
    vehicle_type = models.CharField(max_length=100, choices= vehicle_type)
    charge = models.IntegerField()
    
    def __str__(self):
        return self.vehicle_type


class VehicleInformationModel(models.Model):
    color = models.CharField(max_length=100)
    vehicle_number_plate = models.CharField(max_length=10)
    brand = models.CharField(max_length=100)
    vehicle_owner = models.CharField(max_length=100)
    vehicle_owner_email = models.EmailField(max_length=100)
    vehicle_type = models.ForeignKey(VehicleTypeModel, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.vehicle_number_plate


        
