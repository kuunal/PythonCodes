from .models import ParkingSlotModel
from django.core.exceptions import ValidationError

def get_slots():
    try:
        current_slot_position = ParkingSlotModel.objects.latest(id)
    except current_slot_position.DoesNotExist:
        return 1
    else:
        if  ParkingSlotModel.objects.latest(id) > 400:
            return current_slot_position+1 
        else:
            ParkingSlotModel.objects.first(driver=None)

