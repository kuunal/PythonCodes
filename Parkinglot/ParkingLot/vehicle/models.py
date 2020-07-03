from django.db import models

# Create your models here.

class VehicleInformationModel(models.Model):
    color = models.CharField(max_length=100)
    vehicle_number_plate = models.CharField(max_length=10)
    brand = models.CharField(max_length=100)
    vehicle_owner = models.CharField(max_length=100)
    vehicle_owner_email = models.EmailField(max_length=100)

    def __str__(self):
        return self.vehicle_number_plate