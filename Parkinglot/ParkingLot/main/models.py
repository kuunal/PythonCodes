from django.db import models
from staff.models import UserModel, RoleModel     
from django.contrib.auth.models import User

vehicle_type= (
    ('car','car'),
    ('bike','bike')
)
class VehicleTypeModel(models.Model):
    vehicle_type = models.CharField(max_length=100, choices= vehicle_type)
    charge = models.IntegerField()
    
    def __str__(self):
        return self.vehicle_type

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
    vehicle_number = models.CharField(max_length= 10,null= False)
    vehicle_type = models.ForeignKey(VehicleTypeModel, on_delete=models.DO_NOTHING)
    entry_time = models.DateTimeField(auto_now=True)
    parking_type = models.ForeignKey(ParkingTypeModel, on_delete=models.DO_NOTHING)
    driver_type = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)
    disabled = models.BooleanField(default=False)
    exit_time = models.DateTimeField(auto_now=False, auto_now_add=False)


driver_type=(
        ('driver','driver'),
        ('police','police'),
        ('security','security'),
        ('owner','owner')
    )

class ParkingSlotModel(models.Model):
    slot_id = models.IntegerField()
    driver= models.ForeignKey(User, on_delete=models.DO_NOTHING)
    parking_type= models.ForeignKey(ParkingTypeModel, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.parking_slot

class ParkingLotModel(models.Model):
    slot_id= models.ForeignKey(ParkingSlotModel,default=None, on_delete=models.DO_NOTHING)
    parking_type= models.ForeignKey(ParkingTypeModel, on_delete=models.DO_NOTHING)
    driver= models.CharField(max_length= 100, choices= driver_type)

    