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
from vehicle.models import VehicleInformationModel as Vehicle

DEFAULT_CHARGES = 15

def get_current_user():
    redis_instance = get_redis_instance()
    for key in redis_instance.scan_iter():
        return key.decode('utf-8')

def unpark(instance):
    slot_object = get_object_or_404(slot,slot_id=instance.parking_slot)
    if slot_object.vehicle_number == "null" :
        raise ValidationError("No such vehicle parked!")
    vehicle_number = slot_object.vehicle_number
    total_charges = calculate_charges(instance, vehicle_number)
    slot_object.vehicle_number = None
    slot_object.save()
    tasks.send_mail_to_user_when_vehicle_is_unparked.delay(instance.vehicle_number.vehicle_owner_email, total_charges)
    return total_charges

def calculate_charges(instance, vehicle_number):
    parking_type_charge = instance.parking_type.charge
    vehicle_type_charge = Vehicle.objects.get(vehicle_number_plate=vehicle_number).vehicle_type.charge
    instance.exit_time = timezone.now()
    entry_time = instance.entry_time
    instance.save()
    total_parked_time = (instance.exit_time-instance.entry_time)
    total_hours = total_parked_time.total_seconds()//(60*60)

    if total_hours > 1 :
        total_hours*2
    return DEFAULT_CHARGES + vehicle_type_charge + parking_type_charge + total_hours + get_object_or_404(RoleModel, user=instance.driver_type).charge
