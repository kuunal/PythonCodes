from .models import ParkingSlotModel
from django.core.exceptions import ValidationError

def get_slot():
    try:
        current_slot_position = ParkingSlotModel.objects.latest(id)
    except Exception:
        return 1
    else:
        if  ParkingSlotModel.objects.latest(id) < 400:
            return current_slot_position+1 
        else:
            if ParkingSlotModel.objects.first(driver=None) == None:
                raise ValidationError("Lot Full")

