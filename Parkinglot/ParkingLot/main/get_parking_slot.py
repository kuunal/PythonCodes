from .models import ParkingSlotModel as slot
from .models import ParkingLotModel as lot 
from django.core.exceptions import ValidationError
from . import tasks
from django.contrib.auth.models import User


def get_slot(): 
    total_slot = lot.objects.all().values_list('total_slots')[0][0]
    total_floor = lot.objects.all().values_list('total_floors')[0][0]
    slot_per_floor = total_slot//total_floor
    unparked_slot = slot.objects.filter(vehicle_number="null").first()
    occupied_slots = slot.objects.count()
    if unparked_slot == None and occupied_slots == 0:
        return 1
    elif unparked_slot == None and occupied_slots >= slot_per_floor:
        tasks.send_mail_to_owner_when_lot_is_full(occupied_slots//slot_per_floor)
        if slot.objects.count() == total_slot:
            raise ValidationError("Lot Full")   
    if unparked_slot:
        return unparked_slot.id
    else:
        return slot.objects.latest('id').id + 1  
    # pass
