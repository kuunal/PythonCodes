from django.shortcuts import get_object_or_404
from .models import ParkingSlotModel as slot
from .models import ParkingTypeModel
from datetime import datetime
from django.utils import timezone
from status_code import get_status_codes
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from register.models import RoleModel
from . import tasks
from ParkingLot.redis_setup import get_redis_instance


DEFAULT_CHARGES = 15

    # def is_authentic(func):
    #     def wrapper(request, *args, **kwargs):
    #         redis_instance = get_redis_instance()
    #         for key in redis_instance.scan_iter():
    #             if key == None:
    #                 return Response(400)
    #             func(request, *args, **kwargs)
    #         return wrapper

def unpark(instance):
    slot_object = get_object_or_404(slot,slot_id=instance.parking_slot)
    if slot_object.vehicle_number == "null" :
        raise ValidationError("No such vehicle parked!")
    
    total_charges = calculate_charges(instance)
    print(total_charges)
    slot_object.vehicle_number = "null"
    slot_object.save()
    tasks.send_mail_to_user_when_vehicle_is_unparked.delay(instance.vehicle_number.vehicle_owner_email, total_charges)
    return total_charges

def calculate_charges(instance):
    parking_type_charge = instance.parking_type.charge
    vehicle_type_charge = instance.vehicle_type.charge
    instance.exit_time = timezone.now()
    entry_time = instance.entry_time
    instance.save()
    print(instance.exit_time, instance.entry_time)
    total_parked_time = (instance.exit_time-instance.entry_time)
    total_hours = total_parked_time.total_seconds()//(60*60)

    if total_hours > 1 :
        total_hours*2

    return DEFAULT_CHARGES + vehicle_type_charge + parking_type_charge + total_hours + get_object_or_404(RoleModel, user=instance.driver_type).charge
