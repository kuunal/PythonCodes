from django.contrib import admin
from .models import ParkingModel, ParkingTypeModel, VehicleTypeModel, ParkingSlotModel, ParkingLotModel
# Register your models here.
admin.site.register(ParkingModel)
admin.site.register(ParkingTypeModel)
admin.site.register(VehicleTypeModel)
admin.site.register(ParkingSlotModel)
admin.site.register(ParkingLotModel)

