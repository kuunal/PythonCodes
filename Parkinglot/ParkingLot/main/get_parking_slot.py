from .models import ParkingSlotModel as slot
from django.core.exceptions import ValidationError

def get_slot():
    unparked_slot = slot.objects.filter(vehicle_number="null").first()
    if unparked_slot == None and slot.objects.count() == 0:
        return 1
    elif unparked_slot == None and slot.objects.count() == 400:
        raise ValidationError("Lot Full")
    elif unparked_slot:
        return unparked_slot.id
    else:
        return slot.objects.latest('id').id + 1  
    # pass
