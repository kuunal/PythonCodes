from .models import ParkingSlotModel as slot
from .models import ParkingLotModel as lot 
from django.core.exceptions import ValidationError
from . import tasks
from django.contrib.auth.models import User


def get_slot(): 
    total_slot = lot.objects.all().values_list('total_slots')[0][0]
    total_floor = lot.objects.all().values_list('total_floors')[0][0]
    slot_per_floor = total_slot//total_floor
    slot_per_floor_list = get_slot_list(total_slot, total_floor)
    unparked_slot = slot.objects.filter(vehicle_number="null").first()
    initialized_slots = slot.objects.count()
    if unparked_slot == None and initialized_slots == 0:
        return 1
    elif unparked_slot == None and initialized_slots >= total_slot:
        tasks.send_mail_to_owner_when_lot_is_full(" ")
        raise ValidationError("Lot Full")
    if unparked_slot:
        send_mail_to_floor(unparked_slot, slot_per_floor_list, slot_per_floor)
        return unparked_slot.id
    else:
        send_mail_to_floor(slot.objects.latest('id') , slot_per_floor_list, slot_per_floor)
        return slot.objects.latest('id').id + 1  
        # pass

def send_mail_to_floor(unparked_slot, slot_per_floor_list, slot_per_floor):
    floor = [ str(slot_per_floor_list.index(slot)) for slot in slot_per_floor_list if (unparked_slot.id + 1) % slot_per_floor == 0 and (unparked_slot.id + 1) > slot]
    print(floor,"sadasdasdasdasdasdasdasdasdasd")
    if len(floor) > 0:
        floors_full = ","
        floors_full = floors_full.join(floor)
        tasks.send_mail_to_owner_when_lot_is_full.delay(floors_full)

def get_slot_list(total_slot, total_floor):
    slot_per_floor = total_slot//total_floor
    slot_at_each_floor = slot_per_floor
    slot_per_floor_list = []
    for slot in range(total_floor):
        slot_per_floor_list.append(slot_at_each_floor)
        slot_at_each_floor += slot_per_floor
    return slot_per_floor_list