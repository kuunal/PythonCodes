from django.shortcuts import get_object_or_404
from .models import ParkingSlotModel as slot
from .models import ParkingTypeModel
from datetime import datetime


# def is_authentic(token):
#     redis_instance = get_redis_instance()
#     for key in redis_instance.scan_iter():
#         if redis_instance.get(key).decode('utf-8') == token:
#             return key
#         return False
DEFAULT_CHARGES = 15

def unpark(instance):
    parking_type_charge = instance.parking_type.charge
    vehicle_type_charge = instance.vehicle_type.charge
    instance.exit_time = datetime.now()
    entry_time = instance.entry_time
    total_parked_time = (instance.exit_time-instance.entry_time)
    total_hours = total_parked_time.total_seconds()/60*60
    slot_object = get_object_or_404(slot,id=instance.id)
    total_charges = calculate_charges(parking_type_charge, vehicle_type_charge, total_parked_time)
    slot_object.vehicle_number = "null"
    slot_object.save()
    return total_charges

def calculate_charges(parking_type_charge, vehicle_type_charge, total_parked_time):
    
    return DEFAULT_CHARGES + vehicle_type_charge + parking_type_charge + total_parked_time
    
