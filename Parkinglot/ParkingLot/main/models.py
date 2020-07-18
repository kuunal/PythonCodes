from django.db import models
from register.models import  RoleModel     
from django.contrib.auth.models import User
from datetime import datetime
from vehicle.models import VehicleInformationModel as vehicle
from vehicle.models import VehicleTypeModel

parking_type=(
    ('own','own' ),
    ('vallet','vallet')
)
class ParkingTypeModel(models.Model):
    parking_type = models.CharField(max_length=10, choices=parking_type)
    charge = models.IntegerField()

    def __str__(self):
        return self.parking_type

class ParkingModel(models.Model):
    parking_slot = models.IntegerField(null= False)
    vehicle_number = models.ForeignKey(vehicle,on_delete=models.CASCADE)
    entry_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    parking_type = models.ForeignKey(ParkingTypeModel, on_delete=models.DO_NOTHING)
    driver_type = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)
    disabled = models.BooleanField(default=False)
    exit_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True )
    
    def __str__(self):
        return f'{self.parking_slot} {self.vehicle_number}'



driver_type=(
        ('driver','driver'),
        ('police','police'),
        ('security','security'),
        ('owner','owner')
    )

class ParkingSlotModel(models.Model):
    slot_id = models.IntegerField()
    vehicle_number = models.ForeignKey(vehicle, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f'{self.slot_id} {self.vehicle_number} '

class ParkingLotModel(models.Model):
    total_slots = models.IntegerField()
    total_floors = models.IntegerField()


            